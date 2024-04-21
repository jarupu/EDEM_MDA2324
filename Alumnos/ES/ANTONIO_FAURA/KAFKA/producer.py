import time
from confluent_kafka import Producer
import csv
import json

# Configuración producer
config = {
    'bootstrap.servers': 'localhost:9092', 
    'client.id': 'python-producer'
}

# Creación producer
producer = Producer(config)
topic_kafka = 'fumadores.uklandia'  

with open('fumadores_uklandia.csv') as file:  
    
    reader = csv.DictReader(file, delimiter=",")
    for count, line in enumerate(reader):
        time.sleep(2)
        print(line)

        data_json = json.dumps(line)

        #(Codificación)
        data_bytes = data_json.encode('utf-8')

        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)
        producer.flush()