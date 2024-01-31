class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

    def mostrar_datos(self):
        print(f"NIF: {self.nif}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Aprobado: {'Sí' if self.aprobado else 'No'}")

class GestorAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self):
        nif = input("Ingrese el NIF del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        apellidos = input("Ingrese los apellidos del alumno: ")
        telefono = input("Ingrese el teléfono del alumno: ")
        email = input("Ingrese el email del alumno: ")
        nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
        self.alumnos.append(nuevo_alumno)
        print("Alumno agregado con éxito.")

    def eliminar_alumno(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                self.alumnos.remove(alumno)
                print("Alumno eliminado con éxito.")
                return
        print("No se encontró ningún alumno con ese NIF.")

    def actualizar_datos_alumno(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.nombre = input(f"Nuevo nombre para {alumno.nombre}: ")
                alumno.apellidos = input(f"Nuevos apellidos para {alumno.apellidos}: ")
                alumno.telefono = input(f"Nuevo teléfono para {alumno.telefono}: ")
                alumno.email = input(f"Nuevo email para {alumno.email}: ")
                print("Datos actualizados con éxito.")
                return
        print("No se encontró ningún alumno con ese NIF.")

    def mostrar_datos_alumno_nif(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.mostrar_datos()
                return
        print("No se encontró ningún alumno con ese NIF.")

    def mostrar_datos_alumno_email(self, email):
        for alumno in self.alumnos:
            if alumno.email == email:
                alumno.mostrar_datos()
                return
        print("No se encontró ningún alumno con ese Email.")

    def listar_todos_alumnos(self):
        print("Lista de todos los alumnos:")
        for alumno in self.alumnos:
            alumno.mostrar_datos()

    def aprobar_alumno(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.aprobado = True
                print("Alumno aprobado con éxito.")
                return
        print("No se encontró ningún alumno con ese NIF.")

    def suspender_alumno(self, nif):
        for alumno in self.alumnos:
            if alumno.nif == nif:
                alumno.aprobado = False
                print("Alumno suspendido con éxito.")
                return
        print("No se encontró ningún alumno con ese NIF.")

    def mostrar_alumnos_aprobados(self):
        print("Alumnos aprobados:")
        for alumno in self.alumnos:
            if alumno.aprobado:
                alumno.mostrar_datos()

    def mostrar_alumnos_suspendidos(self):
        print("Alumnos suspendidos:")
        for alumno in self.alumnos:
            if not alumno.aprobado:
                alumno.mostrar_datos()

if __name__ == "__main__":
    gestor = GestorAlumnos()

    while True:
        print("\nMenú:")
        print("(1) Añadir un alumno")
        print("(2) Eliminar alumno por NIF")
        print("(3) Actualizar datos de un alumno por NIF")
        print("(4) Mostrar datos de un alumno por NIF")
        print("(5) Mostrar datos de un alumno por Email")
        print("(6) Listar TODOS los alumnos")
        print("(7) Aprobar Alumno por NIF")
        print("(8) Suspender Alumno por NIF")
        print("(9) Mostrar alumnos aprobados")
        print("(10) Mostrar alumnos suspendidos")
        print("(X) Finalizar Programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.agregar_alumno()
        elif opcion == "2":
            nif_eliminar = input("Ingrese el NIF del alumno a eliminar: ")
            gestor.eliminar_alumno(nif_eliminar)
        elif opcion == "3":
            nif_actualizar = input("Ingrese el NIF del alumno a actualizar: ")
            gestor.actualizar_datos_alumno(nif_actualizar)
        elif opcion == "4":
            nif_mostrar = input("Ingrese el NIF del alumno a mostrar: ")
            gestor.mostrar_datos_alumno_nif(nif_mostrar)
        elif opcion == "5":
            email_mostrar = input("Ingrese el Email del alumno a mostrar: ")
            gestor.mostrar_datos_alumno_email(email_mostrar)
        elif opcion == "6":
            gestor.listar_todos_alumnos()
        elif opcion == "7":
            nif_aprobar = input("Ingrese el NIF del alumno a aprobar: ")
            gestor.aprobar_alumno(nif_aprobar)
        elif opcion == "8":
            nif_suspender = input("Ingrese el NIF del alumno a suspender: ")
            gestor.suspender_alumno(nif_suspender)
        elif opcion == "9":
            gestor.mostrar_alumnos_aprobados()
        elif opcion == "10":
            gestor.mostrar_alumnos_suspendidos()
        elif opcion.upper() == "X":
            break
        else:
            print("Opción no válida. Intente de nuevo.")