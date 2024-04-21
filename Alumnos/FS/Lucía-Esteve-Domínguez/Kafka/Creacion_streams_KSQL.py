import requests
import json

def creacion_streams():
    ksql_url = "http://ksql-server:8088/ksql"
    headers = {
        "Content-Type": "application/vnd.ksql.v1+json",
        "Accept": "application/vnd.ksql.v1+json"
    }
    def send_ksql_command(command):
        payload = {"ksql": command, "streamsProperties": {}}
        response = requests.post(ksql_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Command '{command}' executed successfully.")
            print(response.json())
        else:
            print(f"Error executing command '{command}'")
            print(response.text)
    commands = [
        "CREATE STREAM Recepcion_avisos (tipo_prenda VARCHAR, precio DOUBLE, fecha VARCHAR, contacto VARCHAR) WITH (KAFKA_TOPIC='Recepcion_avisos', VALUE_FORMAT='JSON');",
        "CREATE STREAM Redireccion_Sueters WITH (KAFKA_TOPIC='Sueters', VALUE_FORMAT='JSON') AS SELECT * FROM Recepcion_avisos WHERE tipo_prenda='Sueter';",
        "CREATE STREAM Redireccion_Faldas WITH (KAFKA_TOPIC='Faldas', VALUE_FORMAT='JSON') AS SELECT * FROM Recepcion_avisos WHERE tipo_prenda='Faldas';",
        "CREATE STREAM Redireccion_Zapatos WITH (KAFKA_TOPIC='Zapatos', VALUE_FORMAT='JSON') AS SELECT * FROM Recepcion_avisos WHERE tipo_prenda='Zapatos';",
        "CREATE STREAM Redireccion_Vestidos WITH (KAFKA_TOPIC='Vestidos', VALUE_FORMAT='JSON') AS SELECT * FROM Recepcion_avisos WHERE tipo_prenda='Vestidos';",
    ]
    for command in commands:
        send_ksql_command(command)

