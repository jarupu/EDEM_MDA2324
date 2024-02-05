class Alumno:
    def __init__(self, nif, nombre, apellidos, telefono, email, aprobado=False):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.aprobado = aprobado

# Lista para almacenar los alumnos
lista_alumnos = []

def agregar_alumno():
    nif = input("Introduce el NIF del alumno: ")
    nombre = input("Introduce el nombre del alumno: ")
    apellidos = input("Introduce los apellidos del alumno: ")

    telefono = input("Introduce el teléfono del alumno: ")
    email = input("Introduce el email del alumno: ")

    nuevo_alumno = Alumno(nif, nombre, apellidos, telefono, email)
    lista_alumnos.append(nuevo_alumno)
    print(f"Alumno {nombre} {apellidos} añadido correctamente")

def eliminar_alumno():
    nif_eliminar = input("Introduce el NIF del alumno a eliminar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif_eliminar:
            lista_alumnos.remove(alumno)
            print(f"Alumno con NIF {nif_eliminar} eliminado correctamente")
            return
    print(f"No se encontró ningún alumno con NIF {nif_eliminar}")

def actualizar_datos_alumno():
    nif_actualizar = input("Introduce el NIF del alumno a actualizar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif_actualizar:
            # Solicitar nuevos datos al usuario
            alumno.nombre = input("Nuevo nombre: ")
            alumno.apellidos = input("Nuevos apellidos: ")
            alumno.telefono = input("Nuevo teléfono: ")
            alumno.email = input("Nuevo email: ")
            print(f"Datos del alumno con NIF {nif_actualizar} actualizados correctamente")
            return
    print(f"No se encontró ningún alumno con NIF {nif_actualizar}")

def mostrar_datos_alumno_nif():
    nif_mostrar = input("Introduce el NIF del alumno a mostrar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif_mostrar:
            print("Datos del alumno:")
            print(f"NIF: {alumno.nif}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Email: {alumno.email}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print(f"No se encontró ningún alumno con NIF {nif_mostrar}")

def mostrar_datos_alumno_email():
    email_mostrar = input("Introduce el email del alumno a mostrar: ")
    for alumno in lista_alumnos:
        if alumno.email == email_mostrar:
            print("Datos del alumno:")
            print(f"NIF: {alumno.nif}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Apellidos: {alumno.apellidos}")
            print(f"Teléfono: {alumno.telefono}")
            print(f"Email: {alumno.email}")
            print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")
            return
    print(f"No se encontró ningún alumno con email {email_mostrar}")

def listar_todos_alumnos():
    print("Listado de todos los alumnos:")
    for alumno in lista_alumnos:
        print(f"NIF: {alumno.nif}")
        print(f"Nombre: {alumno.nombre}")
        print(f"Apellidos: {alumno.apellidos}")
        print(f"Teléfono: {alumno.telefono}")
        print(f"Email: {alumno.email}")
        print(f"Aprobado: {'Sí' if alumno.aprobado else 'No'}")

def aprobar_alumno():
    nif_aprobar = input("Introduce el NIF del alumno a aprobar: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif_aprobar:
            alumno.aprobado = True
            print(f"Alumno con NIF {nif_aprobar} aprobado correctamente")
            return
    print(f"No se encontró ningún alumno con NIF {nif_aprobar}")

def suspender_alumno():
    nif_suspender = input("Introduce el NIF del alumno a suspender: ")
    for alumno in lista_alumnos:
        if alumno.nif == nif_suspender:
            alumno.aprobado = False
            print(f"Alumno con NIF {nif_suspender} suspendido correctamente")
            return
    print(f"No se encontró ningún alumno con NIF {nif_suspender}")

def mostrar_alumnos_aprobados():
    print("Alumnos aprobados:")
    for alumno in lista_alumnos:
        if alumno.aprobado:
            print(f"{alumno.nombre} {alumno.apellidos} - NIF: {alumno.nif}")

def mostrar_alumnos_suspendidos():
    print("Alumnos suspendidos:")
    for alumno in lista_alumnos:
        if not alumno.aprobado:
            print(f"{alumno.nombre} {alumno.apellidos} - NIF: {alumno.nif}")

# Menú Principal
while True:
    print("Menú Principal:")
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

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        agregar_alumno()
    elif opcion == '2':
        eliminar_alumno()
    elif opcion == '3':
        actualizar_datos_alumno()
    elif opcion == '4':
        mostrar_datos_alumno_nif()
    elif opcion == '5':
        mostrar_datos_alumno_email()
    elif opcion == '6':
        listar_todos_alumnos()
    elif opcion == '7':
        aprobar_alumno()
    elif opcion == '8':
        suspender_alumno()
    elif opcion == '9':
        mostrar_alumnos_aprobados()
    elif opcion == '10':
        mostrar_alumnos_suspendidos()
    elif opcion.lower() == 'x':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
