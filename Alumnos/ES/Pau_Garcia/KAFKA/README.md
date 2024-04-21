# Entregable kafka 
## Caso de uso: 
Tenemos un radar localizado cerca de un aeródromo, y utilizamos streams de kafka para monitorizar la situación de las aeronaves que entran en nuestro espacio de operaciones.

Cuando una nave entra en el espacio del radar, este genera un mensaje que manda a los dispositivos de los ATC. El mensaje contiene algunas características relevantes como el identificador del vuelo, altura y velocidad en aire. 

Las consultas ksql que podríamos llegar a hacer son una lista muy extensa: desde localizar objetos no identificados, comprobar que una nave no está incumpliendo normas de velocidad o altura en distintas partes del espacio que abarca el radar,... 

En nuestra demo hemos rastreado los vuelos que están a más de 25000 pies y van a más de 380 nudos. 

## Ejecutar la solución:
Navega hasta el directorio de este archivo y ejecuta la siguiente linea por terminal:
`docker compose up -d`

A continuación puedes ejecutar:
`docker exec -it kafka-ksql-cli-1 ksql http://localhost:8088`

Si el servidor ksql se muestra como no válido en el CLI, podemos resolverlo accediendo a él desde el contenedor con la IP interna.
`docker inspect <nombre_contenedor_cli>`
Esta linea te devolverá las características de la red que utilizan nuestros servicios.
Por ejemplo:
`docker exec -it kafka-ksql-cli-1 ksql http://172.18.0.4:8088`

Ahora ya deberías poder crear un stream y hacer queries sobre él.
- STREAM:
`CREATE STREAM flight_radar (flight_number VARCHAR, airspeed INT, current_height INT) WITH (kafka_topic='points', value_format='JSON');`

- QUERY:
`SELECT * FROM flight_radar WHERE (current_height > 25000) AND (airspeed > 380) emit changes;
`