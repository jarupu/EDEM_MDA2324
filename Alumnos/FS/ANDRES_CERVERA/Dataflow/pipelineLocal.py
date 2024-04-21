import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse
import json
import logging
import requests
from google.cloud import bigquery
from google.cloud import vision

class ParsePubSubMessage(beam.DoFn):
    def process(self, element):
        message = json.loads(element)
        # Eliminar el campo 'image_url' si está presente
        message.pop('image_url', None)
        yield message

class FormatResults(beam.DoFn):
    def __init__(self, radar_id, cars_api):
        self.radar_id = radar_id
        self.cars_api = cars_api

    def process(self, element):
        # Obtener la URL de la imagen del coche multado de la API
        car_data = self._get_car_data()
        image_url = car_data.get("image_url", "no multado")

        # Obtener la matrícula del coche multado de la imagen
        license_plate = self._get_license_plate(image_url)

        # Evaluar si el coche está multado o no
        is_fined = element["avg_speed"] > 40
        if not is_fined:
            license_plate = "no multado"
            image_url = "no multado"

        formatted_message = {
            "radar_id": self.radar_id,
            "vehicle_id": element.get("vehicle_id", ""),
            "avg_speed": element.get("avg_speed", 0.0),
            "is_fined": is_fined,
            "license_plate": license_plate,
            "image_url": image_url
        }
        yield formatted_message

    def _get_car_data(self):
        # Hacer la solicitud a la API para obtener la imagen del coche multado y la matrícula
        response = requests.get(self.cars_api)

        if response.status_code == 200:
            # La solicitud fue exitosa, obtener los datos del coche de la respuesta JSON
            car_data = response.json()
            return car_data
        else:
            # Si la solicitud no fue exitosa, registrar el error y devolver None
            logging.error("Failed to retrieve car data from API: %s", response.text)
            return None

    def _get_license_plate(self, image_url):
        # Use Cloud Vision API to detect license plate from image URL
        if image_url == "no multado":
            return "no multado"

        client = vision.ImageAnnotatorClient()
        image = vision.Image()
        image.source.image_uri = image_url
        response = client.text_detection(image=image)
        texts = response.text_annotations
        if texts:
            for text in texts:
                if len(text.description) > 5 and any(c.isdigit() for c in text.description) and any(c.isalpha() for c in text.description):
                    return text.description
        return None

class CalculateAvgSpeed(beam.DoFn):
    def process(self, element):
        vehicle_id, msgs = element
        avg_speed = sum(msg['speed'] for msg in msgs) / len(msgs)
        yield {'vehicle_id': vehicle_id, 'avg_speed': avg_speed}

class WriteToBigQuery(beam.DoFn):
    def __init__(self, table_spec, is_fined):
        self.table_spec = table_spec
        self.is_fined = is_fined

    def process(self, element):
        if self.is_fined and element["is_fined"]:
            self._write_to_bigquery(element, self.table_spec)
        elif not self.is_fined and not element["is_fined"]:
            self._write_to_bigquery(element, self.table_spec)

    def _write_to_bigquery(self, element, table_spec):
        # Write message to the specified BigQuery table
        row = element
        try:
            bigquery_client = bigquery.Client()
            dataset_ref = bigquery_client.dataset(table_spec.datasetId, project=table_spec.projectId)
            table_ref = dataset_ref.table(table_spec.tableId)
            table = bigquery_client.get_table(table_ref)

            errors = bigquery_client.insert_rows_json(table, [row])

            if errors:
                logging.error("Errors occurred while inserting data into BigQuery: %s", errors)
            else:
                logging.info("Data successfully inserted into BigQuery.")
        except Exception as e:
            logging.error("Error while inserting data into BigQuery: %s", str(e))

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id', required=True, help='Project ID')
    parser.add_argument('--input_subscription', required=True, help='Input subscription')
    parser.add_argument('--output_topic', required=True, help='Output topic')
    parser.add_argument('--radar_id', required=True, help='Radar ID')
    parser.add_argument('--cars_api', required=False, help='Cars API URL')
    known_args, pipeline_args = parser.parse_known_args(argv)

    fined_table_spec = beam.io.gcp.bigquery.TableReference(
        projectId=known_args.project_id,
        datasetId='dataflowdataset',
        tableId='procesado-fined'
    )

    nonfined_table_spec = beam.io.gcp.bigquery.TableReference(
        projectId=known_args.project_id,
        datasetId='dataflowdataset',
        tableId='procesado-non-fined'
    )

    options = PipelineOptions(pipeline_args)
    options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=options) as pipeline:
        messages = (
            pipeline
            | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
            | 'Parse PubSub messages' >> beam.ParDo(ParsePubSubMessage())
        )

        # Aplicar una ventana fija de 60 segundos a los datos
        windowed_messages = messages | 'Apply fixed window' >> beam.WindowInto(beam.window.FixedWindows(60))

        # Agrupar los mensajes por vehicle_id dentro de la ventana de tiempo fija
        grouped_messages = windowed_messages | 'Group by vehicle_id' >> beam.GroupBy(lambda x: x['vehicle_id'])

        # Calcular la velocidad media para cada grupo
        avg_speed_per_vehicle = grouped_messages | 'Calculate avg speed' >> beam.ParDo(CalculateAvgSpeed())

        formatted_data = avg_speed_per_vehicle | 'Format results' >> beam.ParDo(FormatResults(known_args.radar_id, known_args.cars_api))

        # Write fined messages to BigQuery table
        _ = (
            formatted_data
            | 'Write fined data to BigQuery' >> beam.ParDo(WriteToBigQuery(fined_table_spec, is_fined=True))
        )

        # Write non-fined messages to BigQuery table
        _ = (
            formatted_data
            | 'Write non-fined data to BigQuery' >> beam.ParDo(WriteToBigQuery(nonfined_table_spec, is_fined=False))
        )

        # Encode data and write to Pub/Sub topic
        encoded_data = formatted_data | 'Encode data to byte string' >> beam.Map(lambda x: json.dumps(x).encode('utf-8'))
        _ = encoded_data | 'Write to PubSub' >> beam.io.WriteToPubSub(topic=known_args.output_topic)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
