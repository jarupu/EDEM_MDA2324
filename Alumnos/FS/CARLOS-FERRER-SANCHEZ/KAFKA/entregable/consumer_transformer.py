from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps

consumer = KafkaConsumer(
    'iot_sensor_data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

for message in consumer:
    data = message.value
    data['isHighConsumption'] = data['energyConsumption'] > 100  

    # Enviar todos los datos a processed_iot_data
    producer.send('processed_iot_data', value=data)
    print(f"Processed data sent: {data}")

    # Si es de alta consumición, enviar a high_consumption_data
    if data['isHighConsumption']:
        producer.send('high_consumption_data', value=data)
        print(f"High consumption data sent: {data}")
