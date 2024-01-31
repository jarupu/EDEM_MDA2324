'''Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
Arrancar
Acelerar
Frenar
Parar'''

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

# Ejemplo de uso
mi_auto = Automovil(marca="Toyota", modelo="Corolla", color="Azul")
mi_auto.arrancar()
mi_auto.acelerar(30)
mi_auto.frenar(10)
mi_auto.parar()