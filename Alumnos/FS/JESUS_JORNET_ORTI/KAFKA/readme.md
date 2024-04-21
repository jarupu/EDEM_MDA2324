# Caso de uso: Kafka para la monitorización en tiempo real de la calidad del aire en Valencia

Trabajamos en la aplicación de Apache Kafka para la recolección, procesamiento y visualización en tiempo real de datos de la calidad del aire desde diversas estaciones de monitoreo en Valencia. Implementa un flujo de datos basado en eventos para capturar y analizar métricas ambientales de manera instantánea.

## Imagen del funcionamiento
![Imagen de Kafka en terminal][Alumnos/FS/JESUS_JORNET_ORTI/KAFKA/Imagen/captura.png]

## Arquitectura y Proceso de Datos

El sistema se basa en una arquitectura que facilita la recolección, el procesamiento y la visualización de datos de calidad del aire a través de las siguientes etapas:

### 1. Recolección de Datos

- **`producer.py`**: Script Python encargado de simular la generación de datos de calidad del aire, incluyendo identificadores de estación (`station_id`), concentraciones de partículas PM10, PM2.5, niveles de NO2, y marcas de tiempo (`timestamp`). Estos datos son publicados en un topic de Kafka destinado a las mediciones brutas de calidad del aire.

### 2. Consumo y Procesamiento de Datos

- **`consumer.py`**: Este componente consume los datos desde el topic de Kafka, preparándolos para su posterior análisis. Los datos pueden ser almacenados para análisis históricos o procesados en tiempo real para monitorizar el calidad del aire.

### 3. Análisis de Datos con KSQL

Se utiliza KSQL para la creación de un stream `air_quality_stream` sobre el topic `processed_air_quality`. Este proceso permite la manipulación y consulta en tiempo real de los datos de calidad del aire:

```sql
CREATE STREAM air_quality_stream (
    station_id STRING,
    pm10 DOUBLE,
    pm2_5 DOUBLE,
    no2 DOUBLE,
    timestamp STRING,
    calidad_aire STRING
) WITH (
    KAFKA_TOPIC='processed_air_quality',
    VALUE_FORMAT='JSON'
);
```

Y luego vemos los datos con la siguiente query:
```ruby
SELECT * FROM air_quality_stream EMIT CHANGES LIMIT 10
```

## Conclusiones

Con este planteamiento para el monitoreo de la calidad del aire en Valencia facilitamos la toma de decisiones al poder monitorizar en tiempo real y almacenar para su posterior análisis.

[Alumnos/FS/JESUS_JORNET_ORTI/KAFKA/Imagen/captura.png]: Alumnos/FS/JESUS_JORNET_ORTI/KAFKA/Imagen/captura.png