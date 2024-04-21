# Ejemplo de Productor-Consumidor Kafka

Esta carpeta contiene un ejemplo simple de un productor y consumidor de Kafka implementados en Python. El propósito de este caso de uso es realizar un ejemplo de cómo utilizar Kafka para la mensajería entre aplicaciones, para el máster de EDEM Data.

## Estructura de la carpeta

La carpeta está estructurada de la siguiente manera:

- `consumer.py`: Un script en Python que consume mensajes de un topic de Kafka.
- `docker-compose.yml`: Archivo de configuración de Docker Compose para orquestar los servicios de Kafka.
- `producer.py`: Un script en Python que produce mensajes y los envía a un topic de Kafka.
- `requirements.txt`: Archivo que contiene las dependencias necesarias para ejecutar los scripts Python.

## Prerrequisitos

Antes de ejecutar este ejemplo, hay que tener Docker instalado en tu sistema.

## Pasos para Ejecutar

1. **Ejecutar Docker Compose**:

    Ejecuta el siguiente comando para iniciar los servicios de Kafka utilizando Docker Compose:

    ```bash
    docker-compose up -d
    ```

2. **Instalar Dependencias**:

    Instala las dependencias necesarias usando pip y el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Crear un topic de Kafka**:

    Utiliza el siguiente comando para crear un topic de Kafka llamado "compras":

    ```bash
    docker-compose exec kafka kafka-topics --create --topic compras --bootstrap-server localhost:9092
    ```

4. **Ejecutar el Productor**:

    Abre una terminal y ejecuta el script `producer.py`:

    ```bash
    python producer.py
    ```

5. **Ejecutar el Consumidor**:

    Abre otra terminal simultáneamente y ejecuta el script `consumer.py`:

    ```bash
    python consumer.py
    ```

6. **Procesar Datos con Kafka SQL**:

    Sin necesidad de haber consumido los mensajes, se pueden leer directamente desde el topic como si fuera un SQL. Primero hay que configurar que lea los mensajes desde el inicio del topic

    ```bash
    SET 'auto.offset.reset' = 'earliest';
    ```

    Después ya se pueden leer estos, como alternativa al uso del `consumer.py`:

     ```bash
    PRINT 'compras' FROM BEGINNING;
    ```


## Notas Adicionales

- Hay que asegurarse de que los servicios de Kafka estén en funcionamiento antes de ejecutar los scripts `producer.py` y `consumer.py`.
- Se pueden modificar los parámetros de configuración de Kafka en el archivo `docker-compose.yml` según tus necesidades.
- Los mensajes producidos por el productor serán consumidos por el consumidor y mostrados en la terminal.
