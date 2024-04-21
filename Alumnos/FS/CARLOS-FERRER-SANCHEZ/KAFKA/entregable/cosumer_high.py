from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'high_consumption_data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    data = message.value
    print(f"Received high consumption data: {data}")
