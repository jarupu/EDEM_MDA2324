from confluent_kafka import Consumer, KafkaError, Producer
import json

# Configuración del consumidor y productor
cons_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}

prod_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Creamos consumidor y productor
consumer = Consumer(cons_config)
producer = Producer(prod_config)

# Suscribirse a un topic
topic = 'fumadores_uklandia'  # Cambia el nombre del tema al que te quieres suscribir
consumer.subscribe([topic])

# Consumo
try:
    while True:
        msg = consumer.poll(1.0)  

        if msg is None:
            continue
        if msg.error():
            print("Error al recibir mensaje: {}".format(msg.error()))
            continue

        message_data = json.loads(msg.value().decode('utf-8'))

        # Filtrar los registros por los que fuman ('smoke' == 'Yes')
        if 'smoke' in message_data and message_data['smoke'] == 'Yes':
            # Producir en el topic 'Smokers'
            producer.produce('Smokers', key=msg.key(), value=msg.value())
            print('Smoker: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar consumidor y productor
    consumer.close()
    producer.close()
