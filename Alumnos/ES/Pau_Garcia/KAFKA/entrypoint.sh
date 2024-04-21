#!/bin/bash

# Retrieve the IP address of the Kafka service
KAFKA_IP=$(getent hosts kafka | awk '{ print $1 }')

# Set the Kafka IP address as an environment variable
export KAFKA_BOOTSTRAP_SERVERS="$KAFKA_IP:9092"

# Run your Python application
exec python producer.py
