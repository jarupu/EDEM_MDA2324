import time
import random
from collections import Counter

def mostrar_palabra_adivinada(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def obtener_frecuencia_letras():
    palabras_comunes = ['ACTIVIDADES', 'PYTHON', 'PROYECTO', 'AHORCADO', 'ALEATORIO', 'PALABRA', 'JUEGO']
    todas_las_letras = [letra for palabra in palabras_comunes for letra in palabra]
    frecuencia_letras = Counter(todas_las_letras)
    letras_ordenadas = [letra for letra, _ in frecuencia_letras.most_common()]
    return letras_ordenadas

def jugador_automatico():
    letras = obtener_frecuencia_letras()

    tiempo_inicio_juego = time.time()
    intentos = 0
    errores = 0

    palabra = random.choice(['ACTIVIDADES', 'PYTHON', 'PROYECTO', 'AHORCADO', 'ALEATORIO', 'PALABRA', 'JUEGO'])
    letras_adivinadas = set()

    print("\nINICIA JUGADOR AUTOMÁTICO\n")

    while not set(palabra).issubset(letras_adivinadas) and errores < 5:
        letra = letras.pop(0) if letras else random.choice(letras)

        intentos += 1

        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f" La letra '{letra}' está en la palabra")
        else:
            errores += 1
            print(f" La letra '{letra}' no está en la palabra. Errores: {errores}/5")

        print(" Palabra actual: ", mostrar_palabra_adivinada(palabra, letras_adivinadas))
        time.sleep(1)  # Pausa entre intentos

    tiempo_fin_juego = time.time()
    tiempo_juego = tiempo_fin_juego - tiempo_inicio_juego

    if errores == 5:
        print(f"\nEL JUGADOR AUTOMÁTICO HA ALCANZADO EL LÍMITE DE ERRORES. La palabra era '{palabra}': En {intentos} intentos y un total de {tiempo_juego:.2f} segundos!")
    else:
        print(f"\n¡Palabra adivinada por el jugador automático: '{palabra}' en {intentos} intentos y un total de {tiempo_juego:.2f} segundos!")

if __name__ == "__main__":
    jugador_automatico()
