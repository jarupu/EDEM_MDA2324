import json
import os
import time
import pandas as pd
import random
from confluent_kafka import Producer

def generatedata():
    global counter
    counter=counter+1
    if counter>=len(lines):
        counter=0
    data={}
    data["userid"]=user_id
    data["timestamp"]=int(time.time())
    data["heart_rate"]=lines[counter]*100+random.randint(0,100)
    return json.dumps(data)

def senddata():
    # Coloca el código para enviar los datos a tu sistema de mensajería
    # Utiliza la variable topic id para especificar el topico destino
    producer.produce(topic=topic_kafka,value=generatedata(), key=user_id)
    producer.flush()
    print(generatedata())

if __name__ == '__main__':
    user_id= 'asd'#os.getenv('USER_ID')
    topic_id= 'asd' #os.getenv('TOPIC_ID')
    time_lapse= 3 #int(os.getenv('TIME_ID'))

    # Config del Producer para el servidor Kafka
    config = {
        'bootstrap.servers': 'kafka:29092',  # Ojo si se ejecuta en un container
        'client.id': 'python-producer'
    }
    # Crear un productor
    producer = Producer(config)
    # Utiliza la variable topic id para especificar el topico destino
    topic_kafka = 'end2end_edem'

    counter=0
    lines=[]

    with open('data/data.csv', 'r') as file:
        lines = file.readlines()

    lines = [float(line.strip()) for line in lines]
        
    print(lines)


    while True:
        senddata()
        time.sleep(time_lapse)
