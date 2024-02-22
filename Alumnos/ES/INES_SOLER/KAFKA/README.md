# PostWork Kafka: Ventas Online
Este caso de uso se basa en los datos de venta online de una empresa guardados en el [Archivo csv](./sales_data.csv).

Primero, levantamos todos los contenedores necesarios con el comando:
```
docker-compose up -d
```

Una vez están corriendo todos correctamente, creamos los topics a los que queremos enviar mensajes (los registros de ventas). 
Yo creé los dos topics desde la terminal con los comandos:

```
docker-compose exec kafka kafka-topics --create --topic sales --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

```
docker-compose exec kafka kafka-topics --create --topic selected_categories --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

El paso siguiente es ejecutar el script del productor para que lea los mensajes que van llegando y los envíe al topic 'sales' y después, ejecutar el script del consumidor. 
El consumidor está diseñado para que lea los mensajes del topic 'sales' y envíe al topic 'selected_categories' solo las ventas de productos que pertenecen a la categoria de 'Alimentation' o a la de 'Sports'.

Los mensajes se envían en formato JSON y contienen los siguientes datos de la venta:
```
{
  "Order Date": "2019-01-13 23:51:00",
  "Order ID": "141314",
  "Product": "Macbook Pro Laptop",
  "Product_ean": "2892197004217.0",
  "catégorie": "Sports",
  "Purchase Address": "700 Jefferson St, New York City, NY 10001",
  "Quantity Ordered": "1",
  "Price Each": "1700.0",
  "Cost price": "561.0",
  "turnover": "1700.0",
  "margin": "1139.0"
}
```

Comprobamos que tanto el productor como el consumidor están enviando mensajes cada pocos segundos y abrimos KSQL en la terminal con el siguiente comando:

```
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
```

Y aquí es donde filtramos las ventas de los productos de Alimentación y Deportes y filtramos aquellas con un margen superior a 40, las cuales se guardan en otro topic llamado 'higher40'.

De esta forma creamos un proceso que ayude a la empresa en la toma de decisiones al poder seleccionar las ventas de las categorías que sean de más/menos interés y analizar los productos que tengan un margen más alto o más bajo.

Las pruebas de que la aplicación funciona y el resultado de cada paso se encuentran en la carpeta [Capturas](./screenshots)

