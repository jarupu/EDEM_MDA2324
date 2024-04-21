from confluent_kafka.admin import AdminClient, NewTopic

def creacion_topics():
    admin_client = AdminClient({
        "bootstrap.servers": "kafka:29092"
    })
    topic_names = ["Recepcion_avisos","Sueters","Faldas","Zapatos","Vestidos"] 
    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in topic_names]
    futures = admin_client.create_topics(new_topics)
    for topic, future in futures.items():
        try:
            future.result()  
            print(f"Topic {topic} creado con éxito.")
        except Exception as e:
            print(f"No se pudo crear el topic {topic}: {e}")