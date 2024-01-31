import time
import random

def mostrar_palabra_adivinada(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def obtener_letra():
    while True:
        letra = input("  Di una letra (o escribe 'ME RINDO' para terminar el juego): ").upper()
        if letra == "ME RINDO" or (len(letra) == 1 and letra.isalpha()):
            return letra
        else:
            print("Entrada no válida. Por favor, ingresa una letra o 'ME RINDO'.")

while True:
    print("\n\nVAMOS A JUGAR AL MARAVILLOSO JUEGO DEL AHORCADO\n")
    time.sleep(1) 

    palabras = ['ACTIVIDADES', 'PYTHON', 'PROYECTO', 'AHORCADO', 'ALEATORIO', 'PALABRA', 'JUEGO']
    letras = ["A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    intentos_totales = 0
    tiempo_total = 0

    jugar_otra_vez = True

    while jugar_otra_vez:
        # Comienza el juego
        tiempo_inicio_juego = time.time()
        intentos = 0
        errores = 0

        # Selecciona una palabra aleatoria
        palabra = random.choice(palabras)
        letras_adivinadas = set()

        while not set(palabra).issubset(letras_adivinadas) and errores < 5:
            letra = obtener_letra()

            if letra == "ME RINDO":
                print(f"\nTe has rendido. La palabra era '{palabra}'. Has intentado {intentos} intentos sin conseguir adivinar la palabra.")
                break

            intentos += 1

            if letra in palabra:
                letras_adivinadas.add(letra)
                print(f" La letra '{letra}' está en la palabra")
            else:
                errores += 1
                print(f" La letra '{letra}' no está en la palabra. Errores: {errores}/5")

            print(" Palabra actual: ", mostrar_palabra_adivinada(palabra, letras_adivinadas))

        if letra != "ME RINDO":
            tiempo_fin_juego = time.time()
            tiempo_juego = tiempo_fin_juego - tiempo_inicio_juego
            tiempo_total += tiempo_juego

            if errores == 5:
                print(f"\nHAS ALCANZADO EL LÍMITE DE ERRORES. ¡ERES UN MANTA! La palabra era '{palabra}'")
            else:
                print(f"\n¡Palabra adivinada: '{palabra}' en {intentos} intentos y un total de {tiempo_juego:.2f} segundos!")

        respuesta = input("\n  ¿Quieres jugar otra vez? (Sí/No): ").upper()
        while respuesta not in ["S", "SI", "N", "NO"]:
            print("Respuesta no válida. Por favor, ingresa 'Sí' o 'No'.")
            respuesta = input("\n  ¿Quieres jugar otra vez? (Sí/No): ").upper()

        if respuesta in ["N", "NO"]:
            print("\nHAS DEJADO DE JUGAR AL NO TAN MARAVILLOSO PARA TI JUEGO DEL AHORCADO")
            jugar_otra_vez = False
        else:
            print("\nVEO QUE TE GUSTA EL JUEGUECITO, ¡JUGUEMOS DE NUEVO!\n")

    if respuesta in ["N", "NO"]:
        break 

if intentos_totales == 0:
    print("\nUN ABRAZO XIMO.")
else:
    print(f"\nTotales: Adivinaste en {intentos_totales} intentos y un total de {tiempo_total:.2f} segundos.")
