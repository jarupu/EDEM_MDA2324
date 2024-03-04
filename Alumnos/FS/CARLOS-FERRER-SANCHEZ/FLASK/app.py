from flask import Flask
from flask_restx import Api, Resource, fields, reqparse, abort

app = Flask(__name__)
api = Api(app, version='1.0', title='Sensor Temperature API',
          description='API para monitorear la temperatura de un robot en tiempo real.')

ns = api.namespace('Sensores', description='Operaciones de sensores')

measure_model = api.model('Measure', {
    'code': fields.String(required=True, description='ID del sensor'),
    'fechamuestreo': fields.String(required=True, description='Fecha de la muestra'),
    'unidad': fields.String(required=True, description='Unidad de la medición'),
    'medicion': fields.Float(required=True, description='Valor de la medición'),
})

# Datos de muestra para la "base de datos" en memoria
DB = {
    'sensor1': {'code': 'sensor1', 'fechamuestreo': '2024-02-15T12:34:56', 'unidad': 'Celsius', 'medicion': 22.5},
    'sensor2': {'code': 'sensor2', 'fechamuestreo': '2024-02-15T13:34:56', 'unidad': 'Celsius', 'medicion': 23.5},
}

@ns.route('/getLastMeasureBySensor/<string:sensor>')
@ns.response(404, 'Sensor no encontrado')
@ns.response(400, 'ID del sensor no válido')
@ns.param('sensor', 'El ID del sensor')
class Sensor(Resource):
    @ns.doc('get_last_measure')
    @ns.marshal_with(measure_model)
    def get(self, sensor):
        """Inserta una nueva medición para un sensor específico."""
        # Validación básica del ID del sensor
        if sensor is None or sensor not in DB:
            abort(404, 'Sensor no encontrado')
        return DB[sensor]
    
    @ns.doc('create_measure')
    @ns.expect(measure_model)
    @ns.marshal_with(measure_model, code=201)
    def post(self, sensor):
        """Inserta una nueva medición para un sensor específico."""
        # Validación básica del ID del sensor
        if sensor is None or not sensor.strip():
            abort(400, 'ID del sensor no válido')
        
        # Obtener los datos del cuerpo de la solicitud
        data = api.payload
        if 'code' not in data or data['code'] != sensor:
            abort(400, 'ID del sensor no coincide con el cuerpo de la solicitud')
        
        # Asumiendo que fechamuestreo, unidad y medicion están presentes en los datos de la solicitud
        DB[sensor] = data
        return data, 201

if __name__ == '__main__':
    app.run(debug=True)
