golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}


clavesTecnico = ("admin", "CCCDDD", "2020")
golosinasPedidas = []


opcion = ''
while opcion != 'd':
    print('\n====MAQUINA DE CARAMELOS====')
    print('a. Pedir golosina')
    print('b. Mostrar golosinas')
    print('c. Rellenar golosinas')
    print('d. Apagar maquina')
    

    opcion = input('Seleccione una opción: ').lower()

    if opcion == 'a':
        legajo = int(input('Di tu numero de legajo: '))
        if legajo not in empleados:
            print('Usted no es un empleado de la empresa')
        else:
            print('Bienvenido/a', empleados[legajo])

            pedir_golosina = True
            while pedir_golosina:
  
                codigo_de_golosina = input("Ingrese el código de la golosina (o 'salir' para finalizar): ")
                
                if codigo_de_golosina.lower() == 'salir':
                    pedir_golosina = False
                else:
                    codigo = int(codigo_de_golosina)

                    golosina_encontrada = False
                    for i in golosinas:
                        if i[0] == codigo:
                            golosina_encontrada = True

                            if i[2] <= 0:
                                print(f'Lo sentimos la golosina {i[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina')
                            else:

                                i[2] -= 1
                                print(f'Toma tu golosina {i[1]}')

                                registrada_golosina = False
                                for pedida in golosinasPedidas:
                                    if pedida[0] == codigo:
                                        pedida[2] += 1
                                        registrada_golosina = True
                                        break
                                
                                # CORRECCIÓN 4: Pasar como lista [...]
                                if not registrada_golosina:
                                    golosinasPedidas.append([i[0], i[1], 1])

                                pedir_golosina = False
                            break

                    if not golosina_encontrada:
                        print('El código ingresado no existe.')

    elif opcion == 'b':
        for i in golosinas:
            print("Código:", i[0], "| Golosina:", i[1], "| Stock:", i[2])

    elif opcion == 'c':
        # CORRECCIÓN 5: Quitar int() para que coincida con las cadenas de texto
        clave_1 = input('Ingrese clave 1: ')
        clave_2 = input('Ingrese clave 2: ')
        clave_3 = input('Ingrese clave 3: ')

        if clave_1 == clavesTecnico[0] and clave_2 == clavesTecnico[1] and clave_3 == clavesTecnico[2]:
            codigo_para_recargar = int(input('Ingrese el código de la golosina a recargar: '))

            golosina_encontrada = False
            for i in golosinas:
                if i[0] == codigo_para_recargar:
                    golosina_encontrada = True
                    cantidad = int(input('Ingrese la cantidad a recargar (mayor a cero): '))
                    while cantidad <= 0:
                        cantidad = int(input('La cantidad debe ser mayor a cero. Ingrese nuevamente: '))
                    
                    i[2] += cantidad
                    # CORRECCIÓN 3: Cambiado g por i
                    print(f"Se recargó exitosamente. Nuevo stock de {i[1]}: {i[2]}")
                    break
            
            if not golosina_encontrada:
                print('El código ingresado no existe.')
        else:
            print('No tiene permiso para ejecutar la función de recarga')

    elif opcion == 'd':
        total_pedidas = 0
        for pedida in golosinasPedidas:
            # CORRECCIÓN 6: Quitar paréntesis extra
            print("Código:", pedida[0], " Golosina:", pedida[1], " Cantidad pedida:", pedida[2])
            total_pedidas += pedida[2]
        print("Total de golosinas pedidas:", total_pedidas)
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}
notasFinales = []
mejor_promedio_general = -1.0
nombre_mejor_alumno = ""


for legajo, nombre_alumno in alumnos.items():
    print("Alumno:", nombre_alumno)
    

    materias = [
        ["Ciencias", 0.0, 0.0, 0.0],
        ["Historia", 0.0, 0.0, 0.0],
        ["Geografia", 0.0, 0.0, 0.0],
        ["Matematicas", 0.0, 0.0, 0.0],
        ["Fisica", 0.0, 0.0, 0.0]
    ]
    

    nota_mas_alta = -1.0
    materia_mas_alta = ""
    
    suma_notas_finales = 0.0
    

    for m in materias:
        print("\nIngrese las notas para la materia:", m[0])
        

        n1 = float(input("Nota 1: "))
        while n1 < 0 or n1 > 10:
            n1 = float(input("Nota inválida. Ingrese Nota 1 (entre 0 y 10): "))
            

        n2 = float(input("Nota 2: "))
        while n2 < 0 or n2 > 10:
            n2 = float(input("Nota inválida. Ingrese Nota 2 (entre 0 y 10): "))
            

        promedio_materia = (n1 + n2) / 2
        

        m[1] = n1
        m[2] = n2
        m[3] = promedio_materia
        
        print("Nota Final:", promedio_materia)
        

        suma_notas_finales += promedio_materia
        

        if promedio_materia > nota_mas_alta:
            nota_mas_alta = promedio_materia
            materia_mas_alta = m[0]
            
    # Mostrar la lista completa de materias cargadas
    print("\n--- Resumen de materias de", nombre_alumno, "---")
    for m in materias:
        print("Materia:", m[0], " Nota 1:", m[1], " Nota 2:", m[2], " Nota Final:", m[3])
        
    print("\nLa materia con la calificación más alta fue:", materia_mas_alta, "con una nota de:", nota_mas_alta)
    
    # Calcular promedio general del alumno y guardar en notasFinales
    promedio_general = suma_notas_finales / len(materias)
    notasFinales.append([nombre_alumno, promedio_general])
    
    # Evaluar si es el mejor promedio de todos los alumnos
    if promedio_general > mejor_promedio_general:
        mejor_promedio_general = promedio_general
        nombre_mejor_alumno = nombre_alumno

print("PROMEDIOS GENERALES DE TODOS LOS ALUMNOS")
for registro in notasFinales:
    print("Alumno:", registro[0], " Promedio General:", registro[1])

print("El alumno con el MEJOR promedio de todos es:", nombre_mejor_alumno, "con un promedio de:", mejor_promedio_general)
     