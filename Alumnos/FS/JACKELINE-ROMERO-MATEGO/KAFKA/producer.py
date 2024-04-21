
from confluent_kafka import Producer
from faker import Faker
import json
import time

kafka_broker = 'localhost:9092'
kafka_topic = 'incendio-topic'

producer = Producer({'bootstrap.servers': kafka_broker})

fake = Faker()

def generate_sensor_data():
    # Generar datos del sensor
    sensor_data = {
        'timestamp': int(time.time()), 
        'temperatura': fake.pyfloat(min_value=10, max_value=50, right_digits=2),
        'nivel_humo': fake.pyfloat(min_value=0, max_value=100, right_digits=2),
        'concentracion_gases': fake.pyfloat(min_value=0, max_value=50, right_digits=2),
        'nivel_oxigeno': fake.pyfloat(min_value=10, max_value=30, right_digits=2),
        'deteccion_llamas': fake.boolean(),
        'movimiento_vibracion': fake.boolean()
    }
    print("Datos del sensor generados:", sensor_data)  # Mensaje de depuración
    return sensor_data

def delivery_callback(err, msg):
    if err:
        print('Error al enviar el mensaje:', err)
    else:
        print('Mensaje enviado al topic {} [partition {}]'.format(msg.topic(), msg.partition()))

while True:
    sensor_data = generate_sensor_data()
    print("Enviando mensaje al servidor Kafka:", sensor_data)  # Mensaje de depuración
    producer.produce(kafka_topic, json.dumps(sensor_data), callback=delivery_callback)
    time.sleep(1)
