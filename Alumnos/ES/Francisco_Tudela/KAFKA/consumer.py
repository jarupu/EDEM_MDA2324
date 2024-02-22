from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import json

# Config consumidor
cons_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}
# Config productor
prod_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Creamos consumidor y productor
consumer = Consumer(cons_config)
producer = Producer(prod_config)

# Suscribirse a un topic
topic = 'video.games' 
consumer.subscribe([topic])

# Consumo
try:
    while True:
        msg = consumer.poll(1.0)  

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay mas datos de jugadores.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            try:
                message_data = json.loads(msg.value().decode('utf-8'))

        # Filtrar los registros por los que quieren competir
                allowed_categories = ['competition']
                if 'reason_of_play_game' in message_data and message_data['reason_of_play_game'] in allowed_categories:
                    producer.produce('Competitors', key=msg.key(), value=msg.value())
                    print('Competitors: {}'.format(msg.value().decode('utf-8')))

            except Exception as e:
                print(f"Error al procesar el mensaje: {str(e)}")


except KeyboardInterrupt:
    pass
finally:
    # Cerramos consumidor y productor
    consumer.close()
    producer.close()
