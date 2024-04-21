import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import json

def ParsePubSubMessage(message):
    # Decode PubSub message in order to deal with
    pubsub_message = message.decode('utf-8')

    # Convert string decoded in JSON format
    msg = json.loads(pubsub_message)

    # Divide 'location' en 'latitude' y 'longitude'
    msg['latitude'], msg['longitude'] = msg['location']
    del msg['location']

    print(f'Mensaje insertado en BigQuery: {msg}')

    # Return function
    return msg

options = PipelineOptions(
    streaming=True,
    runner='DataflowRunner',
    project='woven-justice-411714',
    region='europe-west10',
    temp_location='gs://bucket-camara/tmp',
    staging_location='gs://bucket-camara/staging',
    enable_streaming_engine=True
)


# Crear el pipeline de Apache Beam
with beam.Pipeline(options=options) as p:
    # Leer mensajes desde Pub/Sub
    messages = (
        p
        | "ReadFromPubSub" >> beam.io.ReadFromPubSub(subscription='projects/woven-justice-411714/subscriptions/camara-input2-sub')
        | "Parse JSON messages" >> beam.Map(ParsePubSubMessage)
        | "Add Window" >> beam.WindowInto(beam.window.FixedWindows(5))  # Ventana de tiempo de 5 segundos
    )
     # Escribir datos en BigQuery
    messages | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
        table="woven-justice-411714:ejemplo.camara_raw",
        schema='vehicle_id:STRING,speed:FLOAT,latitude:FLOAT,longitude:FLOAT',
        create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
    )