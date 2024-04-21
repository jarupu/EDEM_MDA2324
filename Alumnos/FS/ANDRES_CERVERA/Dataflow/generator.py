""" 
Script: Vehicle Data Generator

Description: The generator will publish new records simulating 
different vehicles driving down the streets of NYC.

EDEM. Master Data Analytics 2023/2024
Professor: Javi Briones
"""

""" Import libraries """
import sys  # Importar la librería sys para manejar la señal de interrupción

from google.cloud import pubsub_v1
import threading
import argparse
import logging
import secrets
import random
import string
import json
import time
from google.cloud import bigquery

#Input arguments
parser = argparse.ArgumentParser(description=('Vehicle Data Generator'))

parser.add_argument(
                '--project_id',
                required=True,
                help='GCP cloud project name.')
parser.add_argument(
                '--topic_name',
                required=True,
                help='PubSub topic name.')
parser.add_argument(
                '--initial_coordinates',
                required=True,
                help='Coordinates for the initial point of the section.')
parser.add_argument(
                '--final_coordinates',
                required=True,
                help='Coordinates for the final point of the section.')
parser.add_argument(
                '--dataset_id',
                required=True,
                help='BigQuery dataset ID.')
parser.add_argument(
                '--table_id',
                required=True,
                help='BigQuery table ID.')

args, opts = parser.parse_known_args()

""" Helpful Code """

class PubSubMessages:

    """ Publish Messages in our PubSub Topic """

    def __init__(self, project_id: str, topic_name: str):
        self.publisher = pubsub_v1.PublisherClient()
        self.project_id = project_id
        self.topic_name = topic_name

    def publishMessages(self, message: str):
        json_str = json.dumps(message)
        topic_path = self.publisher.topic_path(self.project_id, self.topic_name)
        self.publisher.publish(topic_path, json_str.encode("utf-8"))
        logging.info("A New vehicle has been monitored. Id: %s", message['vehicle_id'])

    def __exit__(self):
        self.publisher.transport.close()
        logging.info("PubSub Client closed.")

def getVehicleId():

    """ Simulate the vehicle ID.
    Params:
        -
    Returns:
        vehicle_ids (list): Returns a list of alphanumeric strings of 6 digits as the vehicle ID.
    """

    vehicle_ids = []

    for i in range(5):

        str = string.ascii_letters + string.digits
        vehicle_id = ''.join(secrets.choice(str) for _ in range(6))

        vehicle_ids.append(vehicle_id)

    return vehicle_ids

def getVehicleSpeed():

    """ Simulate the vehicle speed.
    Params:
        -
    Returns:
        vehicle_id (int): Returns the speed of the vehicle.
    """

    prob = random.random()

    if prob < 0.75:
        speed = random.uniform(25, 40)
    else:
        speed = random.uniform(40, 90)

    return round(speed, 4)  # Redondear la velocidad a 4 decimales

def getVehicleLocation(i_coord: tuple, f_coord: tuple, points: int):

    """ Simulate the location of the vehicle.
    Params:
        i_coord (tuple): Lat,lon of the initial point of the section.
        f_coord (tuple): Lat,lon of the final point of the section.
        points (int): Number of points/samples we want to analyze
    Returns:
        coordinates (list): List with all the vehicle locations in that section.
    """
    
    i_lat, i_lon = i_coord
    f_lat, f_lon = f_coord

    coordinates = []

    for i in range(points):

        factor = i / (points - 1)
        lat = i_lat + factor * (f_lat - i_lat)
        lon = i_lon + factor * (f_lon - i_lon)

        coordinates.append((round(lat, 4), round(lon, 4)))  # Redondear las coordenadas a 4 decimales

    return coordinates


def vehicleData(project_id: str, topic_name: str, i_coord: tuple, f_coord: tuple, dataset_id: str, table_id: str):

    """ This method will provide all the data that our device will generate.
    Params:
        i_coord (tuple): Lat,lon of the initial point of the section.
        f_coord (tuple): Lat,lon of the final point of the section.
    Returns:
        vehicle_payload (json): Returns a JSON with all the information about
        the vehicle's position, speed, and image.
    Raises:
        Exception: If there's an error generating the mock data or inserting it into the Pub/Sub topic.
    """

    pubsub_class = PubSubMessages(project_id, topic_name)

    # Simulate Vehicle ID
    vehicle_ids: str = getVehicleId()

    # Get Vehicle Location
    coordinates: list = getVehicleLocation(
        i_coord=i_coord,f_coord=f_coord, points=10)

    # Vehicle Payload
    try:

        for id in vehicle_ids: 

            for item in coordinates:

                # Capture Vehicle Speed for each point
                speed: int = getVehicleSpeed()

                vehicle_payload = {
                    "vehicle_id": id,
                    "speed": speed,
                    "latitude": item[0],  # Extraer la latitud de la tupla de ubicación
                    "longitude": item[1]  # Extraer la longitud de la tupla de ubicación
                }

                print(vehicle_payload)

                # Publish to Pub/Sub
                pubsub_class.publishMessages(vehicle_payload)

                # Insert into BigQuery
                bigquery_client = bigquery.Client()
                dataset_ref = bigquery_client.dataset(dataset_id)
                table_ref = dataset_ref.table(table_id)
                table = bigquery_client.get_table(table_ref)

                errors = bigquery_client.insert_rows_json(table, [vehicle_payload])

                if errors:
                    logging.error("Errors occurred while inserting data into BigQuery: %s", errors)
                else:
                    logging.info("Data successfully inserted into BigQuery.")

    except Exception as err:
        logging.error("Error while processing vehicle data: %s", err)



def run_generator(project_id: str, topic_name: str, i_coord: tuple, f_coord: tuple, dataset_id: str, table_id: str):
    """ Method to simulate the frequency at which vehicles circulate.
    Params:
        project_id (str): Google Cloud Project ID.
        topic_name (str): Google Pub Sub Topic Name.
        i_coord (tuple): Lat,lon of the initial point of the section.
        f_coord (tuple): Lat,lon of the final point of the section.
    Returns:
        -
    """
    try:
        while True:

            # Get Vehicle Data
            threads = []
            num_threads = 3
            
            for i in range(num_threads):
            
                # Create Concurrent threads to simulate the random movement of vehicles.
                thread = threading.Thread(target=vehicleData, args=(project_id, topic_name, i_coord, f_coord, dataset_id, table_id))
                threads.append(thread)

            for thread in threads:
                thread.start()

            # Simulate randomness
            time.sleep(random.uniform(1, 10))

    except KeyboardInterrupt:
        logging.info("Detected KeyboardInterrupt. Exiting...")
        sys.exit(0)  # Salir del script después de la interrupción de teclado

if __name__ == "__main__":
    
    # Set Logs
    logging.getLogger().setLevel(logging.INFO)
    
    # Run Generator
    run_generator(
        args.project_id, args.topic_name, eval(args.initial_coordinates), eval(args.final_coordinates), args.dataset_id, args.table_id)
