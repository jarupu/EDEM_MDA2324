import time
from json import dumps
import json
from confluent_kafka import Producer
import os

file_path = 'radar.json'


with open(file_path, 'r') as file:
    location = json.load(file)

# Configuración del productor
config = {
    'bootstrap.servers': '0.0.0.0:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)


topic_kafka = 'points'
 
count = 0

for point in location:
    data_bytes = dumps(point).encode('utf-8')  # Encode string to bytes
    key = str(count)
    producer.produce(topic=topic_kafka, value=data_bytes, key=key) # Send bytes
    print(f'Sending data: {point}')
    # After your loop where you send messages:
    producer.flush()
    time.sleep(5)
      

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")
    

