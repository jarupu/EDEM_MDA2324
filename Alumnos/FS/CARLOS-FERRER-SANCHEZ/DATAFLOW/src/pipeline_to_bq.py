import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import json

project_id = 'principal-iris-416209'
region_id = 'europe-west10'
temp_location_id = 'gs://bucket-gcp-carlos-dataflow/tmp'
staging_location_id = 'gs://bucket-gcp-carlos-dataflow/staging'
subscription_id = 'projects/principal-iris-416209/subscriptions/output_multas-sub'

def process_coordinates(element):
    message = json.loads(element.decode('utf-8'))
    coordinates_str = message['coordinates']
    coordinates = [float(coord) for coord in coordinates_str.strip("[]").split(",")]
    message['latitude'], message['longitude'] = coordinates
    del message['coordinates']
    return message

options = PipelineOptions(
    streaming=True,
    job_name='task-dataflow1',
    runner='DataflowRunner',
    project=project_id,
    region=region_id,
    temp_location=temp_location_id,
    staging_location=staging_location_id,
    enable_streaming_engine=True
)

with beam.Pipeline(options=options) as p:
    messages = (
        p
        | "ReadFromPubSub" >> beam.io.ReadFromPubSub(subscription=subscription_id)
        | "DecodeAndParseMessages" >> beam.Map(process_coordinates)
        | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
            table="principal-iris-416209.task_dataflow.task_dataflow_multas",
            schema='latitude:FLOAT,longitude:FLOAT,radar_id:STRING,vehicle_id:STRING,avg_speed:FLOAT,is_Ticketed:BOOLEAN,image_url:STRING',
            create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        )
    )
