from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import json

# Configuración del consumidor
cons_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  
}
# Configuración del productor
prod_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Crear un consumidor
consumer = Consumer(cons_config)
producer = Producer(prod_config)

# Suscribirse a un tópico
topic = 'sales'  
consumer.subscribe([topic])

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("There are no more sales records in this partition.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            try:
                message_data = json.loads(msg.value().decode('utf-8'))

        # Filtrar registros por categoría
                allowed_categories = ['Alimentation', 'Sports']
                if 'catégorie' in message_data and message_data['catégorie'] in allowed_categories:
                    producer.produce('selected_categories', key=msg.key(), value=msg.value())
                    print('New sale in Alimentation/Sports: {}'.format(msg.value().decode('utf-8')))

            except Exception as e:
                print(f"Error al procesar el mensaje: {str(e)}")
            

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al parar la Applicacion Python
    consumer.close()
