from Creacion_topics import creacion_topics
from Creacion_streams_KSQL import creacion_streams
from Productor_inicial import activar_productor_inicial
import time
import threading

print("Por favor, espera unos segundos")
time.sleep(30)
creacion_topics()
time.sleep(15)
creacion_streams()
time.sleep(10)
activar_productor_inicial()