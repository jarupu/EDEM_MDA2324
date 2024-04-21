## Arquitectura del ejercicio de Kafka

### Productor (`producer.py`):

- Script en Python responsable de generar mensajes y enviarlos al topic de Kafka.
- Utiliza la biblioteca `confluent_kafka` para interactuar con el clúster de Kafka.
- Los mensajes producidos son jsons que cogen valores aleatorios de un array previamente creado.

### Consumidor (`consumer.py`):

- Otro script en Python que consume mensajes del topic de Kafka.
- Utiliza la biblioteca `confluent_kafka` para interactuar con Kafka.
- Después de consumir los mensajes, estos se podrían procesar mediante otras aplicaciones.

### Kafka:

- Plataforma de transmisión distribuida que permite el almacenamiento y procesamiento de flujos de datos en tiempo real.
- Utiliza un modelo de publicación/suscripción para la mensajería entre aplicaciones, donde los productores publican mensajes en topics y los consumidores se suscriben a estos topics para recibir los mensajes.
- En este caso, se utiliza Kafka para facilitar la comunicación entre el productor y el consumidor, permitiendo el intercambio de mensajes de manera eficiente y escalable.

### Kafka SQL:

- Kafka SQL permite realizar consultas y análisis en tiempo real sobre los datos que fluyen a través de Kafka.
- Proporciona una capa de procesamiento adicional para transformar y analizar datos en tiempo real.
- Permite ejecutar consultas SQL sobre los topics de Kafka, lo que facilita el procesamiento y análisis de datos en tiempo real de manera sencilla y escalable.

### Docker Compose:

- Se utiliza para definir y ejecutar la infraestructura como código, en este caso, los servicios de Kafka y Kafka SQL.
- El archivo `docker-compose.yml` especifica cómo los servicios de Kafka y Kafka SQL se ejecutan en contenedores Docker, incluidos los contenedores de ZooKeeper, Kafka y Kafka SQL.
- Proporciona una forma rápida y sencilla de configurar y desplegar los servicios necesarios sin tener que preocuparse por la configuración manual.

### Topic:

- Un topic en Kafka es una categoría a la que se publican mensajes.
- En este ejemplo, se crea un topic llamado "compras" donde el productor publica mensajes y el consumidor los consume.

En resumen, la arquitectura consiste en un productor que genera mensajes, un consumidor que los consume, Kafka que actúa como intermediario para el intercambio de mensajes, Kafka SQL que proporciona capacidades de procesamiento y análisis en tiempo real mediante consultas SQL sobre los datos en los topics de Kafka, y Docker Compose que facilita la ejecución de Kafka, Kafka SQL y ZooKeeper en contenedores Docker para una configuración y despliegue rápidos y reproducibles.
