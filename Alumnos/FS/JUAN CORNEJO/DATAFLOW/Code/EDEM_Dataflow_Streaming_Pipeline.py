# Import Beam Libraries
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
from apache_beam.metrics import Metrics
from apache_beam.ml.inference.base import RunInference, ModelHandler

# Import GCP Libraries
from google.cloud import vision
from google.cloud.storage import Client as StorageClient

# Import Common Libraries
import requests
import io
import argparse
import logging
import json
import re

""" Helpful functions """
def ParsePubSubMessage(message):
    message = message.decode('utf-8')
    try:
        message = json.loads(message)
    except json.JSONDecodeError:
        logging.error("Invalid JSON format")
        return None
    return message

def getVehicleImage(item, api_url):
    response = requests.get(f"{api_url}?vehicle_id={item['vehicle_id']}")
    if response.status_code == 200:
        image_url = response.json().get('image_url')
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # Asegura que image_response.content es de tipo bytes
            gcs_url = upload_image_to_gcs(image_response.content, item['vehicle_id'])
            # Modifica la estructura de item adecuadamente para la siguiente etapa
            return (item, image_response.content)  # Formato esperado por RunInference
    return None

def upload_image_to_gcs(image_content, vehicle_id, bucket_name="bucket_entregables", folder_name="fotos_vehiculos_multados/"):
    # Use StorageClient that was imported at the top of your script
    client = StorageClient()
    bucket = client.bucket(bucket_name)
    blob_name = f"{folder_name}{vehicle_id}.jpg"
    blob = bucket.blob(blob_name)
    blob.upload_from_string(image_content, content_type='image/jpeg')
    return f"gs://{bucket_name}/{blob_name}"

class CloudVisionModelHandler(ModelHandler):
    def load_model(self):
        client = vision.ImageAnnotatorClient()
        return client

    def run_inference(self, batch, model):
        feature = vision.Feature(type=vision.Feature.Type.TEXT_DETECTION)
        images = [vision.Image(content=image_bytes) for _, image_bytes in batch]
        requests = [vision.AnnotateImageRequest(image=image, features=[feature]) for image in images]
        responses = model.batch_annotate_images(requests=requests)
        for response, (item, _) in zip(responses.responses, batch):
            if response.error.message:
                logging.error(f"Error processing image: {response.error.message}")
                continue
            texts = [annotation.description for annotation in response.text_annotations]
            yield (item, texts) 

class OutputFormatDoFn(beam.DoFn):
    def process(self, element):
        item, texts = element
        license_plate_pattern = r'[A-Z]{3}\d{3,4}'
        found_plates = [text for text in texts if re.match(license_plate_pattern, text)]
        item['license_plate'] = found_plates[0] if found_plates else "no valid plate found"
        yield item

class AvgSpeedDoFn(beam.DoFn):
    def __init__(self, radar_id):
        self.radar_id = radar_id

    def process(self, element):
        key, group = element
        speeds = [item['speed'] for item in group]
        avg_speed = sum(speeds) / len(speeds) if speeds else 0
        output = {'vehicle_id': key, 'avg_speed': avg_speed, 'radar_id': self.radar_id}
        if avg_speed > 40:
            yield beam.pvalue.TaggedOutput('fined_vehicles', output)
        else:
            yield beam.pvalue.TaggedOutput('non_fined_vehicles', output)

""" Dataflow Process """

def run():
    """ Input Arguments"""
    parser = argparse.ArgumentParser(description=('Arguments for the Dataflow Streaming Pipeline.'))
    parser.add_argument('--project_id', required=True, help='GCP cloud project name.')
    parser.add_argument('--input_subscription', required=True, help='PubSub subscription from which we will read data from the generator.')
    parser.add_argument('--output_topic', required=True, help='PubSub Topic which will be the sink for our data.')
    parser.add_argument('--radar_id', required=True, help="Radar ID corresponding to the student's name.")
    parser.add_argument('--cars_api', required=True, help="API for retrieving vehicle images.")
    args, pipeline_opts = parser.parse_known_args()

    options = PipelineOptions(pipeline_opts, save_main_session=True, streaming=True, project=args.project_id)

    with beam.Pipeline(options=options) as p:
        data = (p
                | "Read From PubSub" >> beam.io.ReadFromPubSub(subscription=args.input_subscription)
                | "Parse JSON messages" >> beam.Map(ParsePubSubMessage))

        processed_data = (data 
                | "Extract vehicle id data" >> beam.Map(lambda x: (x['vehicle_id'], x))
                | "User-window based on each vehicle" >> beam.WindowInto(window.FixedWindows(60))
                | "Group by ID" >> beam.GroupByKey()
                | "Avg Speed" >> beam.ParDo(AvgSpeedDoFn(args.radar_id)).with_outputs('fined_vehicles', 'non_fined_vehicles', main='main_output'))

        fined_vehicles = (processed_data.fined_vehicles
                | "Capture Vehicle image" >> beam.FlatMap(lambda x: getVehicleImage(x, args.cars_api))
                | "Model Inference" >> RunInference(CloudVisionModelHandler())
                | "Output Format" >> beam.ParDo(OutputFormatDoFn())
                | "Encode fined_vehicles to Bytes" >> beam.Map(lambda x: json.dumps(x).encode('utf-8'))
                | "Write fined_vehicles to PubSub" >> beam.io.WriteToPubSub(topic=args.output_topic))

        non_fined_vehicles = (processed_data.non_fined_vehicles
                | "Encode non_fined_vehicles to Bytes" >> beam.Map(lambda x: json.dumps(x).encode('utf-8'))
                | "Write non_fined_vehicles to PubSub" >> beam.io.WriteToPubSub(topic=args.output_topic))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info("The process started")
    run()