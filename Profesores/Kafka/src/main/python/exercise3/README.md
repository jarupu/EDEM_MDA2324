# EXCERCISE 1 Confluent Cloud + Python 

## Target
Send messaged with Python from your computer into Kafka Cloud.

## Run
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

Status: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab1_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab1_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

### Command Line Producer

Run the command line producer:

```sh
$ docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>hi
>dlp
>


Alternative:

$ docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>{messageID:1, message:"hi"}
>{messageID:2, message:"dlp"}
>

```

Read topic content:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
hi
dlp
```


Alternative:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
>{messageID:1, message:"hi"}
>{messageID:2, message:"dlp"}
>
```


--------------------------------------------------------------



### Python Example

Before running the example, you need to install the python kafka client library:

```sh
$ pip install kafka-python
$ pip install confluent_kafka
```


The example is based on two python scripts:

* Producer: The producer will generate 100 messages and send them to the `myTopic`. 
* Consumer: Consume and log messages from `myTopic`.  

### Run the python scripts 
Execute the Consumer: run the script consumer.py
Execute the Producer: run the script producer.py


#### Exercises 

* Modify the python Producer script (producer.py) and send different messages. Verify in the Consumer (command line or 
  Consumer script) that you can read/consume the new messages.
*  Use a messages more complex than a String. For example a JSON message like this one => {"name":"John", "age": 26} 
where you can increment the message JSON attribute "age" number in each sent message.

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
