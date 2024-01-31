import requests
from .mongo import store_data_in_mongodb

# obtener datos basicos del JSON 

def valenbisi_api(url: str):
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        for i, estacion in enumerate(range(100)):
            clase = datos['results'][i]
            nombre_estacion: str = clase["address"]
            numero:int = clase["number"]
            fecha_hora:str = clase["updated_at"]
            primary_key = (f'{numero}_{fecha_hora}')
            store_data_in_mongodb(clase,nombre_estacion,primary_key)
    else:
        print(f"Error: {status_code}")