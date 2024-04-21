import csv
from confluent_kafka import Consumer, KafkaException

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
consumer.subscribe(["datosnoprocesados"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            msg_value = msg.value().decode('utf-8')
            # Procesamiento del mensaje CSV
            row = msg_value.strip().split(',')  # Suponiendo que los datos del CSV están separados por comas
            tournament, date, series, court, surface, round_, best_of, player_1, player_2, winner, rank_1, rank_2, pts_1, pts_2, odd_1, odd_2, score = row
            
            # Imprimir los datos procesados
            print(f"Tournament: {tournament}, Date: {date}, Series: {series}, Court: {court}, Surface: {surface}, Round: {round_}, Best of: {best_of}, Player 1: {player_1}, Player 2: {player_2}, Winner: {winner}, Rank 1: {rank_1}, Rank 2: {rank_2}, Pts 1: {pts_1}, Pts 2: {pts_2}, Odd 1: {odd_1}, Odd 2: {odd_2}, Score: {score}")
            
except KeyboardInterrupt:
    pass
finally:
    consumer.close()


