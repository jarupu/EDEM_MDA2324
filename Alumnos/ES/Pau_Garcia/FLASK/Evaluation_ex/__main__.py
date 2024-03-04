from flask import Flask, request, jsonify

app = Flask(__name__)

# Your existing route handler for adding a new temperature record
@app.route('/robots/addLastMeassureBySensor/<sensor_id>', methods=['POST'])
def add_temperature_record(sensor_id):
    # Your existing logic to process the posted data
    # ...

    # Assume you have the created record in the 'created_record' variable
    created_record = {
        "sensor_id": sensor_id,
        "date": datetime.utcnow().isoformat(),
        "unit": "fahrenheit degree",
        "temperature": 98.6
    }

    # Return the created record with a status code of 201
    return jsonify(created_record), 201

if __name__ == '__main__':
    app.run(debug=True)
