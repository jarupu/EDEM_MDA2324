import random
import time
import json
from faker import Faker
from datetime import datetime, timedelta
from confluent_kafka import Producer, Consumer, KafkaError

class venta:
    tipo_prenda = [
        "Sueter",
        "Faldas",
        "Zapatos",
        "Vestidos"
        ]
    fake = Faker('es_ES')
    def __init__(self):
        self.tipo_prenda = random.choice(list(venta.tipo_prenda))
        self.precio = round(random.uniform(15.00, 79.99), 2)
        self.fecha = venta.generar_fecha_aleatoria()
        self.contacto = venta.fake.phone_number()
    ultima_fecha = datetime(datetime.now().year - 1, 1, 1)
    @staticmethod
    def generar_fecha_aleatoria(): #Ajustado para que sean aleatorias y cronológicas para la API.
        incremento = timedelta(hours=random.randint(0, 24), minutes=random.randint(0, 59))
        venta.ultima_fecha += incremento
        return venta.ultima_fecha   
    def to_json(self):
        data = self.__dict__.copy()
        data['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return json.dumps(data)

class producer_Kafka:
    def __init__(self, server_address, producer_id, producer_topic):
        self.server_address:str = server_address
        self.client_id:str = producer_id
        self.producer_conf = {
            'bootstrap.servers': server_address,
            'client.id': producer_id
        }
        self.producer = Producer(self.producer_conf)
        self.producer_topic:str = producer_topic
    def send_data_to_kafka(self,data):
        def delivery_report(err, msg):
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
        self.producer.produce(self.producer_topic,data.encode('utf-8'), callback=delivery_report)
        self.producer.poll(0)
        time.sleep(1)
    def flush_producer(self):
        self.producer.flush()