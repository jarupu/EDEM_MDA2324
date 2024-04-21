from json import dumps
from confluent_kafka import Producer
import csv
import time


def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf

def send_message(producer, topic, key, value):
    producer.produce(topic=topic, value=value, key=key)
    print(f"Sending data: {value} to topic {topic}")

props = read_ccloud_config("client.properties")
producer = Producer(props)

csv_file = "dataset tenis.csv"  # Cambia esto al nombre de tu archivo CSV
topic_kafka = 'datosnoprocesados'

try:
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convierte cada fila en una cadena JSON y envíala al tópico Kafka
            data_str = dumps(row)  # Serialize dictionary to a string
            data_bytes = data_str.encode('utf-8')  # Encode string to bytes
            key = row.get('key', '').encode('utf-8')  # Obtén la clave del diccionario o define una clave alternativa
            send_message(producer, topic_kafka, key, data_bytes)
            time.sleep(3)

except Exception as e:
    print(f"Error al leer o enviar datos al tópico Kafka: {str(e)}")

finally:
    producer.flush()
    producer.close()
