from json import dumps, loads
from confluent_kafka import Producer
import time
import random

from json import loads

def cargar_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return loads(file.read())
    except FileNotFoundError:
        return {}

def mandar_datos_kafka(producer, topic, num_messages=30, min_sleep_time=1, max_sleep_time=5):
    nombre_archivo = 'ufc.json'
    eljson = cargar_json(nombre_archivo)

    with open('ufc.json', 'r', encoding='utf-8') as json_file:
        fighters = loads(json_file.read()).get('fighters', [])

    for e, fighters in enumerate(fighters[eljson.get('fighters_count', 0):], start=eljson.get('fighters_count', 0)):
        fighters_message = {
            'name': (fighters.get('name', '')),
            'wins': (fighters.get('wins', '')),
            'loses': (fighters.get('loses', '')),
            'country': (fighters.get('country','')),
            'endings': (fighters.get('endings', ''))
        }
        data_str = dumps(fighters_message).encode('utf-8')
        key = str(e).encode('utf-8')

        producer.produce(topic=topic_ufc, value=data_str, key=key)
        print("Sending data: {} to topic {}".format(fighters_message, topic))

        sleep_time = random.uniform(min_sleep_time, max_sleep_time)
        time.sleep(sleep_time)

    producer.flush()

    if producer.flush() != 0:
        print("Some messages failed to be delivered")


config = {
    'bootstrap.servers': 'kafka:29092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}
producer = Producer(config)

topic_ufc = 'topic_ufc'
mandar_datos_kafka(producer, topic_ufc)