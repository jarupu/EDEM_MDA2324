from python.extraccion_base import valenbisi_api
#from python.mongo import store_data_in_mongodb
import time

URL:str = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100'

intervalo_tiempo = 600

while True:
    try:
        valenbisi_api(URL)
    except Exception as e:
        print("Error: {e}")
    time.sleep(intervalo_tiempo)
    




