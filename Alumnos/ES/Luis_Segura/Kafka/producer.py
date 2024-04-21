import time
from json import dumps
from confluent_kafka import Producer
import csv

config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = Producer(config)

topic_kafka = 'topic_entregable'

csv_file_path = 'datasetramen.csv'

# Aquí manda los mensajes al topic de Kafka UI
def send_to_kafka(message, key):
    producer.produce(topic=topic_kafka, value=message, key=key)
    producer.flush()
    print(f"Mensaje enviado: {topic_kafka}, Key: {key}, Mensaje: {message}")

# Aquí lee el CSV de ramen y envía los datos a Kafka
try:
    with open(csv_file_path, 'r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            time.sleep(2)
            
            message = dumps(row)
            key = row['Review #']

            send_to_kafka(message, key)

except Exception as e:
    print(f"Error: {e}")
