from confluent_kafka import Consumer, KafkaError

kafka_broker = 'localhost:9092'
kafka_topic = 'incendio-topic'

#Configuración consumidor
consumer_conf = {
    'bootstrap.servers': kafka_broker,
    'group.id': 'my_consumer_group',  
    'auto.offset.reset': 'earliest'  
}

# Crear un consumidor
consumer = Consumer(consumer_conf)

# Suscribirse al topic
consumer.subscribe([kafka_topic])

# Iniciar el bucle de consumo
try:
    while True:
        # Esperar hasta que se obtengan mensajes del topic
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # No hay más mensajes disponibles en el topic
                continue
            else:
                # Otro error
                print("Error al recibir mensaje:", msg.error())
                break

        # Procesar el mensaje
        print('Mensaje recibido: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    # Detener el consumidor cuando se recibe una interrupción del teclado
    pass

finally:
    # Cerrar el consumidor
    consumer.close()
