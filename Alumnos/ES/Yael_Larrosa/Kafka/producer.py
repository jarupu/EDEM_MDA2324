import time
from json import dumps
from confluent_kafka import Producer
import re
import csv

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}
# Crear un productor
producer = Producer(config)

# Nombre del topic de Kafka
topic_kafka = 'ventas'

# Nombre del archivo CSV
csv_file_path = 'sales_dataset.csv'

# Función para enviar mensajes al topic de Kafka
def send_to_kafka(message, key):
    producer.produce(topic=topic_kafka, value=message, key=key)
    producer.flush()
    print(f"Enviando mensaje al topic: {topic_kafka}, Key: {key}, Mensaje: {message}")

# Leer el archivo CSV y enviar sus datos a Kafka
try:
    with open(csv_file_path, 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Ignorar la primera fila si es un encabezado

        for row in csv_reader:
            time.sleep(2)
            # Aquí puedes procesar cada fila según tus necesidades
            # En este ejemplo, se envía cada fila completa como un mensaje al topic de Kafka
            message = ','.join(row)  # Concatenar los valores de la fila como una cadena
            key = row[0]  # Se utiliza el primer valor como clave (puedes ajustar esto según tus necesidades)
            
            send_to_kafka(message, key)

except Exception as e:
    print(f"Error: {e}")
'''
# Crear un productor
producer = Producer(config)


topic_kafka = 'ventas'

file1 = open('sales_dataset.csv',encoding="utf8")
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    time.sleep(2)
    print( line.strip() + "\n")
    words = re.findall(r"[\w']+|[.,!?;]", line)
    for word in words:
        data_bytes = word  # Encode string to bytes
        key = str(count)
        producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
        # After your loop where you send messages:
        producer.flush()
      

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")
    '''