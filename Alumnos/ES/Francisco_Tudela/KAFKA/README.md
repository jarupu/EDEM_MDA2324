# PostWork Kafka:
Para este entregable hemos hecho uso de un dataset de Kaggle referente a los motivos por los cuales los gamers juegan [Archivo csv](./VideoGameUsage_Profile.csv).
(Al final ha resultado que el dataset era bastante malo...)

Primero, hemos preparado los script de producer y consumer_producer. EL primer crea el topic y produce los mensajes, el segundo se subscibe al primer topic, lee los mensajes los filtra por las personas que juegan para competir y los manda a un nuevo topic como producer.

A continuación levantamos todos los contenedores necesarios con el comando: docker-compose up -d


Los mensajes se envían en formato JSON y contienen los siguientes datos:
```
{
  "Age": "22",
  "Gender": "Male",
  "student": "Yes",
  "play_video_game": "Yes",
  "favorite_game": "FIFA22",
  "most_played_game": "FIFA22",
  "reason_of_play_game":"competition"
}
```

Comprobamos que tanto el productor como el consumidor están enviando mensajes, hemos aplicado un poll de 1s:

Iniciamos KSQL con el siguiente comando: docker-compose exec ksql-cli ksql http://host.docker.internal:8088

Creamos un topic llamado Fifa y en el instertamos los datos. (La idea era filtar por las personas que competian y luego por juegos, pero como el dataset era tan corto no había suficiente información)

El proceso se ha documentado con imagenes en la carpeta SCREENSHOTS.