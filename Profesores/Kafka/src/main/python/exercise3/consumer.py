from kafka import KafkaConsumer
from json import loads

# # List of available Kafka brokers
# brokers = ["localhost:9092"]
# # brokers = ["localhost:9092", "localhost:9093"]

# # Create a Kafka consumer instance with necessary configurations
# consumer = KafkaConsumer(
#     'myTopic',
#     bootstrap_servers=brokers,
#     auto_offset_reset='earliest',      # start reading from the beginning of the topic
#     enable_auto_commit=True,
#     group_id='my-group',
#     value_deserializer=lambda x: loads(x.decode('utf-8'))
# )

# print("Start Kafka Consumer")

# # Start consuming messages
# for message in consumer:
#     print(f"Received message: {message.value} with key: {message.key.decode('utf-8')}")

from confluent_kafka import Consumer


def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf


props = read_ccloud_config("client.properties")
props["group.id"] = "python-group-1"
props["auto.offset.reset"] = "earliest"

consumer = Consumer(props)
consumer.subscribe(["topic_0"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is not None and msg.error() is None:
            print("key = {key:12} value = {value:12}".format(key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()