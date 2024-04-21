import subprocess
import googlemaps

def obtener_coordenadas(direccion):
    # Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API de Google Cloud
    gmaps = googlemaps.Client(key='AIzaSyDO-oBaaU8isj6Enj0kBvYiPousCR_U_d0')

    # Realiza la solicitud de geocodificación
    resultado = gmaps.geocode(direccion)

    # Verifica si se encontraron resultados y extrae las coordenadas
    if resultado:
        ubicacion = resultado[0]['geometry']['location']
        return ubicacion['lat'], ubicacion['lng']
    else:
        return None

# Direcciones que deseas geocodificar
initial_coordinates = 'Avinguda de Vicent Andrés Estellés 94, 46100 Burjassot, Valencia, Spain'
final_coordinates = 'Poliesportiu de Burjassot, Valencia, Spain'

# Obtiene las coordenadas iniciales y finales
coordenadas_iniciales = obtener_coordenadas(initial_coordinates)
coordenadas_finales = obtener_coordenadas(final_coordinates)

# Imprime las coordenadas
if coordenadas_iniciales and coordenadas_finales:
    print(f"Coordenadas iniciales: {coordenadas_iniciales}")
    print(f"Coordenadas finales: {coordenadas_finales}")

    # Comando para ejecutar generador.py con las coordenadas obtenidas
    generador_command = [
        'python', 'generador.py',
        '--project_id', 'woven-justice-411714',
        '--topic_name', 'camara-input2',
        '--initial_coordinates', f'{coordenadas_iniciales[0]},{coordenadas_iniciales[1]}',
        '--final_coordinates', f'{coordenadas_finales[0]},{coordenadas_finales[1]}'
    ]

    # Ejecutar generador.py
    result = subprocess.run(generador_command)
    print(result)
else:
    print("No se encontraron las coordenadas.")
