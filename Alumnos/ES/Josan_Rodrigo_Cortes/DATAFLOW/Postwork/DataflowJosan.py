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

        

# DoFn

class getVehicleDoFn(beam.DoFn):

    def process(self, element):
        vehicle_id = element['vehicle_id']
        yield(vehicle_id,element)



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
            output_dict['license_plate'] = "Pending"
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
            | "Extract vehicle id data" >> beam.ParDo(getVehicleDoFn())
            | "User-window based on each vehicle" >> beam.WindowInto(window.Sessions(15))
            | "Group by ID" >> beam.GroupByKey()
            | "Avg Speed" >> beam.ParDo(avgSpeedDoFn(radar_id=args.radar_id)).with_outputs('fined_vehicles', 'non_fined_vehicles')
    )
      
        datatobiqq=(
        processed_data.fined_vehicles
          | "Write fined_vehicles to BigQuery" >> beam.io.WriteToBigQuery(
                table=f"{args.project_id}:{args.bq_dataset}.{args.bq_table}",
                schema = "radar_id:STRING, vehicle_id:STRING, avg_speed:FLOAT, coordinates:STRING, is_Ticketed:BOOLEAN, license_plate:STRING",
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