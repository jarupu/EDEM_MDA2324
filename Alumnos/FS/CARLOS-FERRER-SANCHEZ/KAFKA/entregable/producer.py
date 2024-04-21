# Script de Python para generar datos simulados y enviarlos al tópico `iot_sensor_data`
from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

areas = ["oficinas", "lobby", "cafetería"]

while True:
    data = {
        "sensorId": "sensor{}".format(random.randint(1, 100)),
        "area": random.choice(areas),
        "energyConsumption": round(random.uniform(10.0, 200.0), 2),
        "timestamp": "2024-02-22T12:34:56Z"
    }
    producer.send('iot_sensor_data', value=data)
    print(f"Data sent: {data}")
    sleep(5)
