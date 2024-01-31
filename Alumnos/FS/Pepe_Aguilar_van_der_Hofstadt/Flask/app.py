from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Almacén de datos de prueba
temperatures = []

@app.route('/postTestTemperature', methods=['POST'])
def add_temperature():
    """
    Add test temperature
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: JSON payload
        required: true
        schema:
          $ref: '#/components/schemas/Measure'
    responses:
      200:
        description: Successful operation
    """
    data = request.get_json()

    # Asegúrate de que la clave sea 'sensorID' y no 'code'
    sensor_id = data.get('sensorID')
    print(sensor_id)

    # Agregar la temperatura a la lista
    temperatures.append(data)

    return jsonify({"message": "Temperature added successfully"})

    return jsonify({"message": "Temperature added successfully"})

@app.route('/getLastMeassureBySensor/<sensorID>', methods=['GET'])
def get_temperature(sensorID):
    """
    Get the temperature of the robot
    ---
    parameters:
      - name: sensorID
        in: path
        description: sensor ID
        required: true
        type: string
    responses:
      200:
        description: successful operation
        schema:
          $ref: '#/components/schemas/Measure'
      404:
        description: Invalid ID supplied
    """
    try:
        # Buscar la temperatura por ID de sensor
        for temp in temperatures:
            if temp.get('sensorID') == sensorID:
                return jsonify(temp)
        
        return jsonify({"error": "Invalid ID supplied"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Invalid ID supplied"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Sensor not found"}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=99)