from kafka import KafkaProducer
import json
import time
import random

# Configuración del productor
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

"""
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
    """

# Generar datos ficticios sobre la calidad del aire
def generate_air_quality_data():
    data = {
        "station_id": f"valencia{random.randint(1, 5)}",
        "pm10": round(random.uniform(5.0, 50.0), 2),
        "pm2_5": round(random.uniform(3.0, 35.0), 2),
        "no2": round(random.uniform(10.0, 100.0), 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    return data

# Enviar datos al tópico de Kafka
topic_name = 'air_quality'

for _ in range(100):  # Generar 100 registros de calidad del aire
    data = generate_air_quality_data()
    producer.send(topic_name, value=data)
    print(f"Enviado: {data}")
    time.sleep(1)  # Esperar 1 segundo entre envíos

producer.flush()
