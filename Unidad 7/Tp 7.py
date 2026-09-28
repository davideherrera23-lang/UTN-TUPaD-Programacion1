#1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300
#2)
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800

#3)
frutas_sin_precios= list(precios_frutas)

#4)

numeros_telefonicos_almacenados={}
print('*~*~'*5 +'CONTACTOS'+ '~*~*'*5)
for  i in range(1,6):
    nombres_almacenados=input('Por favor ingrese el nombre del contacto: ')
    numeros_almacenados=int(input('Por favor ingrese el numero del contacto: '))
    numeros_telefonicos_almacenados[nombres_almacenados]=numeros_almacenados

nombre_escrito_por_usuario=str(input('Dime el nombre del contacto para mostrarte su numero: '))
if nombre_escrito_por_usuario == nombres_almacenados:
    print(f'El numero telefonico de su contacto es: {numeros_almacenados}.')
else:
    print('Ese nombre no existe.')   

#5)

frase=input('Ingresa una frase: ')
palabras_frase=frase.split()
palabras_unicas=set(palabras_frase)
recuento_palabras = {}
for palabra in palabras_frase:
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1
    else:
        recuento_palabras[palabra] = 1
print(f'Palabras unicas: {palabras_unicas}')
print(f'Recuento de las palabras: {recuento_palabras}')

#6)

alumnos_notas = {}

for i in range(1, 4):
    nombre = input(f'Ingrese el nombre del alumno {i}: ')
    nota1 = float(input(f'Ingrese la nota 1 de {nombre}: '))
    nota2 = float(input(f'Ingrese la nota 2 de {nombre}: '))
    nota3 = float(input(f'Ingrese la nota 3 de {nombre}: '))
    alumnos_notas[nombre] = (nota1, nota2, nota3)

print('*~*~'*5 +'PROMEDIOS'+ '~*~*'*5)
for nombre, notas in alumnos_notas.items():
    promedio = sum(notas) / 3
    print(f'El alumno {nombre} tiene un promedio de: {promedio:.2f}')


#7)
parcial_1 = {101, 103, 105, 108, 110}
parcial_2 = {102, 103, 108, 111, 112}

print('*~*~'*5 +'RESULTADOS PARCIALES'+ '~*~*'*5)
ambos_aprobados = parcial_1.intersection(parcial_2)
print(f'Estudiantes que aprobaron ambos parciales: {ambos_aprobados}')

solo_uno_aprobado = parcial_1.symmetric_difference(parcial_2)
print(f'Estudiantes que aprobaron solo un parcial: {solo_uno_aprobado}')

total_aprobados = parcial_1.union(parcial_2)
print(f'Lista total de estudiantes que aprobaron al menos uno: {total_aprobados}')


#8)
inventario = {'Arroz': 50, 'Fideos': 30, 'Leche': 20}

print('*~*~'*5 +'GESTIÓN DE STOCK'+ '~*~*'*5)
opcion = input('¿Qué desea hacer? (consultar / modificar / agregar): ').lower()

if opcion == 'consultar':
    producto_buscar = input('Ingrese el nombre del producto a consultar: ')
    if producto_buscar in inventario:
        print(f'El stock de {producto_buscar} es de {inventario[producto_buscar]} unidades.')
    else:
        print('El producto no existe en el inventario.')

elif opcion == 'modificar':
    producto_existente = input('Ingrese el producto para sumarle stock: ')
    if producto_existente in inventario:
        cantidad_sumar = int(input('¿Cuántas unidades desea agregar?: '))
        inventario[producto_existente] += cantidad_sumar
        print(f'Stock actualizado. Ahora hay {inventario[producto_existente]} unidades de {producto_existente}.')
    else:
        print('Ese producto no existe. Use la opción "agregar" para productos nuevos.')

elif opcion == 'agregar':
    nuevo_producto = input('Ingrese el nombre del nuevo producto: ')
    if nuevo_producto not in inventario:
        stock_inicial = int(input('Ingrese el stock inicial: '))
        inventario[nuevo_producto] = stock_inicial
        print(f'Producto {nuevo_producto} agregado con éxito.')
    else:
        print('El producto ya existe en el inventario.')


#9) 
agenda_semanal = {
    ('Lunes', '09:00'): 'Clase de Programación 1',
    ('Miércoles', '14:00'): 'Laboratorio de Computación',
    ('Viernes', '18:00'): 'Tutoría de Matemática'
}

print('*~*~'*5 +'CONSULTA DE AGENDA'+ '~*~*'*5)
dia_consulta = input('Ingrese el día a consultar (Ej: Lunes): ')
hora_consulta = input('Ingrese la hora a consultar (Ej: 09:00): ')

clave_busqueda = (dia_consulta, hora_consulta)

if clave_busqueda in agenda_semanal:
    print(f'Actividad programada: {agenda_semanal[clave_busqueda]}')
else:
    print('No hay actividades registradas para ese día y hora.')


#10)
paises_y_capitales = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
capitales_y_paises = {}
for pais, capital in paises_y_capitales.items():
    capitales_y_paises[capital] = pais

print('*~*~'*5 +'DICCIONARIO INVERTIDO'+ '~*~*'*5)
print(f'Diccionario original: {paises_y_capitales}')
print(f'Nuevo diccionario (Capital -> País): {capitales_y_paises}')