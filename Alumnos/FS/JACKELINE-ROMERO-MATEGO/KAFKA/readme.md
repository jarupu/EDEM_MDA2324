# SISTEMA DE MONITOREO DE RIESGOS DE INCENDIO

Hacemos uso de Kafka y KSQL para analizar y filtrar eventos relacionados con la detección de incendios en tiempo real. El sistema permite identificar eventos con un nivel de riesgo elevado y generar alertas para su posterior acción. 

El sistema recopila datos relacionados con la detección de incendios, incluida la temperatura, el nivel de humo, la concentración de gases, el nivel de oxígeno, la detección de llamas y el movimiento y la vibración. Luego, utiliza KSQL para procesar estos datos, calcular un nivel de riesgo para cada evento y filtrar aquellos eventos con un riesgo elevado.

## RECURSOS

* Productor: Publicamos los datos en tiempo real en el topic "incendio-topic" (producer.py).
* Consumidor: Leemos y procesamos datos (consumer.py).
* KSQL: Empleamos KSQL para crear un nuevo stream (riesgo_incendio) en el que añadimos el nivel de riesgo en función de la temperatura, nivel de humo y detección de llamas. 
* Visualización: Presentamos la información procesada en la interfaz de terminal utilizando Visual Studio Code y la UI de Confluent.
  
## ANEXO


1. Producer and Consumer

!(/Users/jackeline/Desktop/KAFKA/images/producer_consumer.png)

2. Confluent

!(/Users/jackeline/Desktop/KAFKA/images/topic1.png)

!(/Users/jackeline/Desktop/KAFKA/images/topic2.png)

3. Iniciamos KSQL

$ docker exec -it kafka-ksql-cli-1 ksql http://kafka-ksql-server-1:8088

!(/Users/jackeline/Desktop/KAFKA/images/inicio_ksql.png)

### Consultas KSQL

```
CREATE STREAM datos_stream (
    timestamp BIGINT,
    temperatura DOUBLE,
    nivel_humo DOUBLE,
    concentracion_gases DOUBLE,
    nivel_oxigeno DOUBLE,
    deteccion_llamas BOOLEAN,
    movimiento_vibracion BOOLEAN
) WITH (
    KAFKA_TOPIC='incendio-topic',
    PARTITIONS=1,
    REPLICAS=1,
    VALUE_FORMAT='JSON'
);
```

```
CREATE STREAM riesgo_incendio AS
SELECT
    *,
    CASE
        WHEN deteccion_llamas = TRUE THEN 'riesgo elevado'
        WHEN temperatura > 38 AND nivel_humo > 70 THEN 'riesgo elevado'
        WHEN temperatura BETWEEN 35 AND 38 AND nivel_humo BETWEEN 60 AND 70 THEN 'riesgo medio'
        ELSE 'riesgo bajo'
    END AS nivel_riesgo
FROM datos_stream;
```

```SELECT * FROM RIESGO_INCENDIO EMIT CHANGES;```

!(/Users/jackeline/Desktop/KAFKA/images/nivel_riesgo.png)


Si queremos extraer sólo aquellos que tienen un riesgo elevado: 

```SELECT * FROM RIESGO_INCENDIO WHERE "NIVEL_RIESGO" = 'riesgo elevado' EMIT CHANGES;```

!(/Users/jackeline/Desktop/KAFKA/images/riesgo_elevado.png)

