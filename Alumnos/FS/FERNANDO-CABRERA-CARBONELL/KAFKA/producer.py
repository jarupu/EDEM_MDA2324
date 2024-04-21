import time
from json import dumps
from confluent_kafka import Producer
from faker import Faker
from datetime import datetime, timedelta

class PackageDeliveryProducer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': 'python-producer'
        }
        self.producer = Producer(self.config)
        self.topic_kafka = 'package_delivery'
        self.faker = Faker('es_ES')

    def generate_package_delivery_data(self):
        current_time = datetime.now()
        delivery_time = current_time + timedelta(days=self.faker.random_int(min=1, max=5))

        package_data = {
            "tracking_number": self.faker.uuid4(),
            "delivery_time": delivery_time.strftime("%Y-%m-%d %H:%M:%S"),
            "destination_city": self.faker.city(),
            "package_weight": self.faker.random_int(min=1, max=20),
            "delivery_status": self.faker.random_element(elements=("En tránsito", "En reparto", "Entregado")),
            "delivery_address": self.faker.address(),
            "delivery_company": self.faker.company(),
            "delivery_driver": self.faker.name(),
            "delivery_vehicle": self.faker.random_element(elements=("Camión", "Furgoneta", "Bicicleta")),
        }
        return package_data

    def send_data_to_kafka(self, data, key):
        data_str = dumps(data)
        data_bytes = data_str.encode('utf-8')
        key_bytes = str(key).encode('utf-8')
        self.producer.produce(topic=self.topic_kafka, value=data_bytes, key=key_bytes)
        print(f"Sending data: {data} to topic {self.topic_kafka}")
        time.sleep(1)

    def flush_producer(self):
        self.producer.flush()

        if self.producer.flush() != 0:
            print("Some messages failed to be delivered")

if __name__ == "__main__":
    package_delivery_producer = PackageDeliveryProducer()

    for i in range(1000):
        package_delivery_data = package_delivery_producer.generate_package_delivery_data()
        package_delivery_producer.send_data_to_kafka(package_delivery_data, i)

    package_delivery_producer.flush_producer()
