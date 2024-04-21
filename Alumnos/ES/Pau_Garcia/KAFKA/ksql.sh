# Access the KSQL CLI in the Docker container
docker exec -it kafka-ksql-cli-1 ksql http://172.18.0.4:8088

# Create a stream from a Kafka topic
CREATE STREAM flight_radar (flight_number VARCHAR, airspeed INT, current_height INT) WITH (kafka_topic='points', value_format='JSON');

# Perform a simple transformation
SELECT * FROM flight_radar WHERE (current_height > 25000) AND (airspeed > 380) emit changes;



