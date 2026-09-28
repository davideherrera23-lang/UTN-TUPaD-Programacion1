import os

#1)
if not os.path.exists("alumnos.txt"):
    archivo = open("alumnos.txt", "w")
    archivo.close()

#2)
lista_alumnos = []
diccionario_alumnos = {}

archivo = open("alumnos.txt", "r")
for linea in archivo:
    linea = linea.strip()
    if linea != "":
        partes = linea.split(";")
        if len(partes) == 4:
            nombre = partes[0].strip()
            apellido = partes[1].strip()
            legajo = partes[2].strip()
            notapromedio = float(partes[3].strip())

            alumno = {
                "nombre": nombre,
                "apellido": apellido,
                "legajo": legajo,
                "notapromedio": notapromedio,
            }

            lista_alumnos.append(alumno)
            diccionario_alumnos[legajo] = alumno
archivo.close()

#3)
opcion = ""
while opcion != "4":
    print("~*~ MENÚ ~*~")
    print("1. Ver alumnos")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":

        if len(lista_alumnos) == 0:
            print("No hay alumnos registrados.")
        else:
            for alumno in lista_alumnos:
                print(
                    f"Nombre: {alumno['nombre']} {alumno['apellido']} | Legajo: {alumno['legajo']} | Nota Promedio: {alumno['notapromedio']}")
    elif opcion == "2":

        nombre = input("Ingrese nombre: ").strip()
        apellido = input("Ingrese apellido: ").strip()
        legajo = input("Ingrese legajo (5 dígitos): ").strip()

        if legajo in diccionario_alumnos:
            print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        else:
            entrada_nota = input("Ingrese nota promedio (1 a 10): ").strip()
            notapromedio = float(entrada_nota)

            archivo = open("alumnos.txt", "a")
            archivo.write(f"{nombre};{apellido};{legajo};{notapromedio}")
            archivo.close()

            nuevo_alumno = {
                "nombre": nombre,
                "apellido": apellido,
                "legajo": legajo,
                "notapromedio": notapromedio,
            }
            lista_alumnos.append(nuevo_alumno)
            diccionario_alumnos[legajo] = nuevo_alumno
            print("Alumno agregado con éxito.")

    elif opcion == "3":

        archivo = open("aprobados.txt", "w")
        for alumno in lista_alumnos:
            if alumno["notapromedio"] >= 6:
                linea = f"{alumno['nombre']};{alumno['apellido']};{alumno['legajo']};{alumno['notapromedio']}"
                archivo.write(linea)
        archivo.close()


        print("\n--- Contenido de aprobados.txt ---")
        archivo = open("aprobados.txt", "r")
        contenido = archivo.read()
        if contenido != "":
            print(contenido.strip())
        else:
            print("No hay alumnos aprobados.")
        archivo.close()

    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")