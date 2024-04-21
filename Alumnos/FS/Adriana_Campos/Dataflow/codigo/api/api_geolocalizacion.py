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
else:
    print("No se encontraron las coordenadas.")
