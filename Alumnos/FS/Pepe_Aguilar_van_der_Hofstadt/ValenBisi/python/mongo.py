import pymongo
from datetime import datetime
import time

def connect_to_mongodb(coleccion):
    # Conéctate a tu instancia de MongoDB (asegúrate de tener MongoDB ejecutándose localmente o especifica la URL de conexión)
    client = pymongo.MongoClient("mongodb://root:example@host.docker.internal:27017/")

    # Selecciona la base de datos y la colección
    db = client["jackypepe"]
    collection = db[coleccion]

    return collection

def store_data_in_mongodb(data, coleccion, primary_key):
    # Conecta a MongoDB
    collection = connect_to_mongodb(coleccion)

    # Crea un documento con datos y una marca de tiempo
    document = {
        "_id": primary_key,
        "data": data
    }
    # Inserta el documento en la colección
    collection.insert_one(document)

if __name__ == "__main__":
    while True:
        # Datos que deseas almacenar en MongoDB
        data_to_store = "Hola, MongoDB!"

        # Llama a la función para almacenar datos en MongoDB
        store_data_in_mongodb(data_to_store)

