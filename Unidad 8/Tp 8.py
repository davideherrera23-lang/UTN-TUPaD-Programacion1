#1)
archivo_productos = 'productos.txt'
linea1 = 'Leche,1500,10\n'
linea2 = 'Tomate,300,20\n'
linea3 = 'Manteca,100,5\n'

with open(archivo_productos, 'w') as archivo:
    archivo.write(linea1)
    archivo.write(linea2)
    archivo.write(linea3)

# 2)
print("~*~ LISTA DE PRODUCTOS ~*~")
with open(archivo_productos, 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        if len(datos) == 3:
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3)
print("~*~ AGREGAR NUEVO PRODUCTO ~*~")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

with open(archivo_productos, 'a') as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}")

print("Producto guardado ")

# 4)
productos = []

with open(archivo_productos, 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        if len(datos) == 3:
            diccionario_producto = {
                'nombre': datos[0],
                'precio': float(datos[1]),
                'cantidad': int(datos[2])
            }
            productos.append(diccionario_producto)

print("\nLista de productos cargada en memoria:")
print(productos)

# 5)
print("\n~*~ BUSCAR PRODUCTO ~*~")
buscado = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for prod in productos:
    if prod['nombre'].lower() == buscado.lower():
        print(f"¡Encontrado! Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: El producto no existe en la lista.")

# 6)
with open(archivo_productos, 'w') as archivo:
    for prod in productos:
        linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}"
        archivo.write(linea)

print("El archivo 'productos.txt' fue actualizado correctamente.")