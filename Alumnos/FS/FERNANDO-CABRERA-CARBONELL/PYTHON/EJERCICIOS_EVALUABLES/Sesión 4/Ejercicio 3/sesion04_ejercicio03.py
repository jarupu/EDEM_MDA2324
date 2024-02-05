# 3. Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API

import requests

url = "https://randomuser.me/api"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    results = data.get("results", [])
    if results:
        user = results[0]
        name = user.get("name", {})
        first_name = name.get("first", "")
        last_name = name.get("last", "")

        print("nombre", first_name)
        print("apellidos", last_name)
    else:
        print("No hay info")

# En el ejemplo ejecutado, nos aparece como resultado nombre: Nicolas y apellidos: French (adjunto captura)