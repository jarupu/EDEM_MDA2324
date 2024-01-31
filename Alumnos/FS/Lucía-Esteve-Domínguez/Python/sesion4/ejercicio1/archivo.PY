'''A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no '''

#Mostrar los numeros primos en un rango 

def mostrar_primos_en_rango(inicio, fin):
    print(f"Números primos en el rango {inicio} - {fin}:")
    for num in range(inicio, fin + 1):
        if es_primo(num):
            print(num)
            
# Función para evaluar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False

    limite = int(numero ** 0.5) + 1
    for i in range(2, limite):
        if numero % i == 0:
            return False
    return True

# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Ejemplos de uso
mostrar_primos_en_rango(1, 100)

numero_evaluado = 17
if es_primo(numero_evaluado):
    print(f"{numero_evaluado} es primo.")
else:
    print(f"{numero_evaluado} no es primo.")

anio_evaluado = 2024
if es_bisiesto(anio_evaluado):
    print(f"{anio_evaluado} es un año bisiesto.")
else:
    print(f"{anio_evaluado} no es un año bisiesto.")