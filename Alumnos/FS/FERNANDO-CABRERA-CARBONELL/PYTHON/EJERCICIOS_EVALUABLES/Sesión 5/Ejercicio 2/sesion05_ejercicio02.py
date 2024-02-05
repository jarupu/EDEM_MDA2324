# Ejercicio 2
# Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
#	1. Arrancar
#	2. Acelerar
#	3. Frenar
#	4. Parar

class Automovil:
    def __init__(self, modelo):
        self.modelo = modelo
        self.en_marcha = False

    def arrancar(self):
        if not self.en_marcha:
            print(f"Arrancando el automóvil {self.modelo}.")
            self.en_marcha = True
        else:
            print(f"El automóvil {self.modelo} ya está en marcha.")

    def acelerar(self):
        if self.en_marcha:
            print(f'Acelerando {self.modelo}.')
        else:
            print(f"No se puede acelerar {self.modelo} porque no está en marcha.")

    def frenar(self):
        if self.en_marcha:
            print(f'Frenando {self.modelo}.')
        else:
            print(f"No se puede frenar {self.modelo} porque no está en marcha.")

    def parar(self):
        if self.en_marcha:
            print(f"Parando el automóvil {self.modelo}.")
            self.en_marcha = False
        else:
            print(f"El automóvil {self.modelo} ya está parado.")