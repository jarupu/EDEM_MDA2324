class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        if not self.encendido:
            print(f"{self.color} {self.marca} {self.modelo} ha arrancado.")
            self.encendido = True
        else:
            print("El automóvil ya está en marcha.")

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += velocidad
            print(f"Acelerando a {self.velocidad} km/h.")
        else:
            print("Primero, arranca el automóvil.")

    def frenar(self, deceleracion):
        if self.encendido:
            self.velocidad = max(0, self.velocidad - deceleracion)
            print(f"Frenando a {self.velocidad} km/h.")
        else:
            print("El automóvil está apagado.")

    def parar(self):
        if self.encendido and self.velocidad == 0:
            print(f"{self.color} {self.marca} {self.modelo} se ha detenido.")
            self.encendido = False
        elif not self.encendido:
            print("El automóvil ya está apagado.")
        else:
            print("Reduce la velocidad antes de detenerte.")

class Coche(Automovil):
    def __init__(self, marca, modelo, color, potencia):
        super().__init__(marca, modelo, color)
        self.potencia = potencia

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += (velocidad + self.potencia)
            print(f"Acelerando a {self.velocidad} km/h.")
        else:
            print("Primero, arranca el coche.")

class Moto(Automovil):
    def __init__(self, marca, modelo, color, potencia):
        super().__init__(marca, modelo, color)
        self.potencia = potencia

class Camion(Automovil):
    def __init__(self, marca, modelo, color, carga_maxima):
        super().__init__(marca, modelo, color)
        self.carga_maxima = carga_maxima

    def frenar(self, deceleracion):
        if self.encendido:
            if self.velocidad - deceleracion > 0:
                self.velocidad -= deceleracion
                print(f"Frenando a {self.velocidad} km/h.")
            else:
                print("El camión ya se ha detenido.")
        else:
            print("El camión está apagado.")