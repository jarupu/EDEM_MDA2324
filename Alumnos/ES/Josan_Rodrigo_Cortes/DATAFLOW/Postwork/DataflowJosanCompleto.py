""" 
Script: Dataflow Streaming Pipeline

Description: This script will be responsible for processing 
messages ingested by our messaging queue from the device and:

    1. Calculate the average speed per vehicle in the section.

    2. Invoke the Vision AI model if the speed exceeds the allowed limit in the section.

    3. Finally, all the information will be sent to another topic for further analysis.

EDEM. Master Data Analytics 2024
Professor: Javi Briones
"""

""" Import libraries """

# Import Beam Libraries

import apache_beam as beam
from apache_beam.runners import DataflowRunner
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
from apache_beam.metrics import Metrics

# Dataflow ML
from apache_beam.ml.inference.base import ModelHandler
from apache_beam.ml.inference.base import RunInference

# Import GCP Libraries
from google.cloud.vision_v1.types import Feature
from google.cloud import vision

# Import Common Libraries
import argparse
import requests
import logging
import json
import re
import io

# beam.options.pipeline_options.PipelineOptions.allow_non_parallel_instruction_output = True
# DataflowRunner.__test__ = True


""" Helpful functions """
def ParsePubSubMessage(message):
    output = message.decode('utf-8')
    return json.loads(output)

def getVehicleImage(item,api_url):

    import requests
    import io

    # API call to simulate a photo captured by the radar
    image_service = requests.get(api_url)
    image_url = json.loads(image_service.content.decode('utf-8'))['image_url']

    #Read image from URL
    image_response = requests.get(image_url)
    image_bytes = io.BytesIO(image_response.content).read()

    #Append image_url to the payload
    item ['image_url'] = image_url

    logging.info(image_url)

    return item, image_bytes   


class CloudVisionModelHandler(ModelHandler):

    def load_model(self):
        
        """Initiate the Google Vision API client."""

        from google.cloud import vision
        from google.cloud.vision_v1.types import Feature
        
        client = vision.ImageAnnotatorClient()
        return client
    
    def run_inference(self, batch, model, inference):

        from google.cloud import vision
        from google.cloud.vision_v1.types import Feature

        from apache_beam.runners import DataflowRunner

        feature = Feature()
        feature.type_ = Feature.Type.TEXT_DETECTION

        images = [vision.Image(content=image_bytes) for (item, image_bytes) in batch]
        item_list = [item for (item, image_bytes) in batch]

        image_requests = [vision.AnnotateImageRequest(image=image, features=[feature]) for image in images]
        batch_image_request = vision.BatchAnnotateImagesRequest(requests=image_requests)

        model_responses = model.batch_annotate_images(request=batch_image_request).responses

        response = model_responses[0].text_annotations
        output_dict = item_list[0]

        license_plate = [text.description for text in response if text.description.isalnum() and not (text.description.isalpha() or text.description.isdigit())]

        
        yield output_dict, license_plate

class OutputFormatDoFn(beam.DoFn):

    def process(self, element):

        output_dict, licnense_plate = element

        if len(licnense_plate) > 0 :

            
            output_dict['license_plate'] = licnense_plate[0] if len(licnense_plate) > 0 else "not recognized"
            
            yield output_dict

        else:

            output_dict['license_plate'] = "no texts found"
            yield output_dict
        

        

# DoFn

class getVehicleDoFn(beam.DoFn):

    def process(self, element):
        vehicle_id = element['vehicle_id']
        yield vehicle_id, element



class avgSpeedDoFn(beam.DoFn):

    def __init__(self,radar_id):

        self.countFinedVehicles = Metrics.counter('main', 'Count of fined vehicles.')
        self.countNonFinedVehicles = Metrics.counter('main', 'Count of non-fined vehicles.')
        self.radar_id = radar_id

    def process(self, element):

        import apache_beam as beam
        import math
        import math

        key, payload = element
        list_coords = []
        list_speeds = []
        list_distances = []
        list_times = []

        for data in payload:
            list_coords.append(data['location'])
            list_speeds.append(data['speed'])

        # Calcular la distancia total
        for i in range(len(list_coords) - 1):
            lat1, lon1 = list_coords[i]
            lat2, lon2 = list_coords[i + 1]

            lat1 = math.radians(lat1)
            lon1 = math.radians(lon1)
            lat2 = math.radians(lat2)
            lon2 = math.radians(lon2)

            # Diferencia de latitud y longitud entre los dos puntos
            dlat = lat2 - lat1
            dlon = lon2 - lon1

            # Fórmula de Haversine
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = 6371 * c  # Radio de la Tierra en kilómetros
            list_distances.append(distance)

            # Calcular el tiempo total
        for d, v in zip(list_distances, list_speeds):
            t = d / v
            list_times.append(t)

        totaltime=sum(list_times)
        totaldistances=sum(list_distances)
        if totaldistances>0 and totaltime>0:

            avg_speed=totaldistances/totaltime
            
            
        else:
            avg_speed=None


        output_dict = {
            "radar_id": "1",
            "vehicle_id": key,
            "avg_speed": avg_speed,
            "coordinates": str(list_coords[-1])
            
        }

        # Create two distinct PCollections, one for fined vehicles and another for those 
        # that have not been fined, so we can process the data differently.

        if avg_speed is not None and avg_speed > 40:
            output_dict['is_Ticketed'] = True
            # output_dict['image_url']="Pending"

            yield beam.pvalue.TaggedOutput('fined_vehicles', output_dict)
        else:
            output_dict['is_Ticketed'] = False
            output_dict['license_plate'] = " Not necessary"
            yield beam.pvalue.TaggedOutput('non_fined_vehicles', output_dict)

""" Dataflow Process """

import argparse
from apache_beam.options.pipeline_options import PipelineOptions

def run():

    """ Input Arguments"""
    parser = argparse.ArgumentParser(description=('Arguments for the Dataflow Streaming Pipeline.'))

    parser.add_argument(
                '--project_id',
                required=False,
                default="prime-apricot-415106",
                help='GCP cloud project name.')
    parser.add_argument(
                '--bucket_id',
                required=False,
                default="entregabledataflow",
                help='Your bucket name.')
    
    parser.add_argument(
                '--input_subscription',
                required=False,
                default="projects/prime-apricot-415106/subscriptions/inputdataflowtopic-sub",
                help='PubSub subscription from which we will read data from the generator.')
    
    
    
    parser.add_argument(
                '--output_subscription',
                required=False,
                default="projects/prime-apricot-415106/topics/outputdataflowtopic",
                help='PubSub Topic which will be the sink for our data.')
    
    parser.add_argument(
                '--radar_id',
                required=False,
                default='josan',
                help='GCP cloud project name.')
    parser.add_argument(
                '--cars_api',
                required=False,
                default='https://europe-west1-long-flame-410209.cloudfunctions.net/car-license-plates-api',
                help="API for retrieving vehicle images.")

    parser.add_argument(
                '--bq_dataset',
                required=False,
                default='vehiculos',
                help='GCP cloud project name.')
    parser.add_argument(
                '--bq_table',
                required=False,
                default='finedVehicles',
                help='GCP cloud project name.')

    args, pipeline_args = parser.parse_known_args()
    
    
    """ Apache Beam Pipeline """
    
    # Pipeline Options
    options = PipelineOptions(
        streaming=True,
        save_main_session=True,
        project=args.project_id,
        runner="DataflowRunner",
        region="europe-southwest1",
        temp_location=f"gs://{args.bucket_id}/temp",
        staging_location=f"gs://{args.bucket_id}/staging",
        input_subscription=args.input_subscription,
        output_subscription=args.output_subscription
    )

    # Pipeline

    with beam.Pipeline(options=options) as p:

        """ Part 01: Read data from PubSub. """

        data = (
                p
                | "Read From Input PubSub" >> beam.io.ReadFromPubSub(subscription=args.input_subscription)
                | "Parse JSON messages" >> beam.Map(ParsePubSubMessage)
            
                
    )

        processed_data = (
            data 
            
            | "Extract vehicle id data" >> beam.ParDo(getVehicleDoFn()) #transformamos el mensaje para agrupar por id
            | "User-window based on each vehicle" >> beam.WindowInto(window.Sessions(15),timestamp_combiner=window.TimestampCombiner.OUTPUT_AT_EOW)
            | "Group by ID" >> beam.GroupByKey()
            | "Avg Speed" >> beam.ParDo(avgSpeedDoFn(radar_id=args.radar_id)).with_outputs('fined_vehicles', 'non_fined_vehicles')
           
    )
    
      
        datatobiqq=(
        processed_data.fined_vehicles
            
            | "Capture Vehicle image" >> beam.Map(getVehicleImage, api_url=args.cars_api)
            | "Model Inference" >> RunInference(model_handler=CloudVisionModelHandler())
            | "Output Format" >> beam.ParDo(OutputFormatDoFn())
            | "Write fined_vehicles to BigQuery" >> beam.io.WriteToBigQuery(
                table=f"{args.project_id}:{args.bq_dataset}.{args.bq_table}",
                schema="radar_id:STRING, vehicle_id:STRING, avg_speed:FLOAT, coordinates:STRING, is_Ticketed:BOOLEAN,  image_url:STRING, license_plate:STRING",
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)


    )
        
        datatopubsub=(
        processed_data.non_fined_vehicles
            
            | "Encode non_fined_vehicles to Bytes" >> beam.Map(lambda x: json.dumps(x).encode("utf-8"))
            | "Write non_fined_vehicles to PubSub" >> beam.io.WriteToPubSub(topic=args.output_subscription)
    )

if __name__ == '__main__':

    # Set Logs
    logging.getLogger().setLevel(logging.INFO)

    logging.info("The process started")

    # Run Process
    run()