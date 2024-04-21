from kafka import KafkaConsumer, KafkaProducer
import json

# Configuración del consumidor
consumer = KafkaConsumer('air_quality',
                         bootstrap_servers=['kafka:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Configuración del productor para enviar datos procesados
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Clasificar la calidad del aire basado en PM2.5
def classify_air_quality(pm2_5):
    if pm2_5 < 12:
        return "Buena"
    elif 12 <= pm2_5 < 35.5:
        return "Moderada"
    else:
        return "Insalubre"

# Leer y procesar mensajes
for message in consumer:
    data = message.value
    print(f"Recibido: {data}")
    
    # Clasificar y agregar la calidad del aire al mensaje
    data['calidad_aire'] = classify_air_quality(data['pm2_5'])
    
    # Reenviar al siguiente topic
    producer.send('processed_air_quality', value=data)
    print(f"Procesado y enviado: {data}")
    producer.flush()


#docker exec -it 9ecc59978786add043c39f386054a8c6a1c8932a0beefebb4b283d845fa44afe ksql http://ksql-server:8088
#docker exec -it entregable-ksql-cli-1 ksql http://kafka-ksql-server-1:8088