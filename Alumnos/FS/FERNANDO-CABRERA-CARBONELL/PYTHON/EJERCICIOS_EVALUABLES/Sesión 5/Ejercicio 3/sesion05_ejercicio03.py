# Ejercicio 3
# 3. Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
#	1. Coche
#	2. Moto
#	3. Camión


class Automovil:
    def __init__(self, modelo):
        self.modelo = modelo
        self.en_marcha = False

    def arrancar(self):
        if not self.en_marcha:
            print(f"Arrancando el {self.modelo}.")
            self.en_marcha = True
        else:
            print(f"El {self.modelo} ya está en marcha.")

    def acelerar(self):
        if self.en_marcha:
            print(f'Acelerando el {self.modelo}.')
        else:
            print(f"No se puede acelerar {self.modelo} si no está en marcha.")

    def frenar(self):
        if self.en_marcha:
            print(f'Frenando el {self.modelo}.')
        else:
            print(f"No se puede frenar {self.modelo} si no está en marcha.")

    def parar(self):
        if self.en_marcha:
            print(f"Parando el {self.modelo}.")
            self.en_marcha = False
        else:
            print(f"El {self.modelo} ya está parado.")

class Coche(Automovil):
    def __init__(self, modelo, potencia):
        super().__init__(modelo)
        self.potencia = potencia

class Moto(Automovil):
    def __init__(self, modelo, potencia):
        super().__init__(modelo)
        self.potencia = potencia

class Camion(Automovil):
    def __init__(self, modelo, potencia):
        super().__init__(modelo)
        self.potencia = potencia