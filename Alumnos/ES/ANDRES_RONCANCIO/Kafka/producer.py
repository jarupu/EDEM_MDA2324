import time
from confluent_kafka import Producer
import csv
import json

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)
topic_kafka = 'movies'

with open('./netflix_titles.csv') as file:
    reader = csv.DictReader(file, delimiter=",")
    for count, line in enumerate(reader):
        time.sleep(2)
        print(line)

        # De diccionario a cadena JSON
        data_json = json.dumps(line)

        # Convertir la cadena JSON a bytes
        data_bytes = data_json.encode('utf-8')

        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        producer.flush()

if producer.flush() != 0:
    print("Some messages failed to be delivered")