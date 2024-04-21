from confluent_kafka import Producer
from Clase_venta import venta
from Clase_venta import producer_Kafka
import json

def activar_productor_inicial():
    def get_data_first_producer():
        registros_ventas = [venta() for _ in range(250)]
        registros_ventas.sort(key=lambda x: x.fecha)
        for ventas_instance in registros_ventas:
            ventas_json = ventas_instance.to_json()
            First_producer.send_data_to_kafka(ventas_json)
    First_producer = producer_Kafka ('kafka:29092','python-producer','Recepcion_avisos')
    get_data_first_producer()
    First_producer.flush_producer()