from flask import Flask, jsonify
import yaml

app = Flask(__name__)

with open('config.yaml', 'r') as file:
    api_spec = yaml.safe_load(file)

sensor_readings = {
    "sensor_01": {
        "timestamp": "2024-01-30T12:00:00Z",
        "value": 20.1
    },
    "sensor_02": {
        "timestamp": "2024-01-30T12:00:00Z",
        "value": 15.5
    }
}

@app.route('/')
def index():
    return '¡La API de Monitoreo Industrial está en funcionamiento!'

@app.route('/sensor/<sensor_id>/last-reading')
def get_last_reading(sensor_id):
    if sensor_id in sensor_readings:
        return jsonify(sensor_readings[sensor_id])
    else:
        return jsonify({"error": "Sensor no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
