#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
edad=int(input("Dime tu edad: "))
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota=int(input("Dime tu nota: "))
if nota < 6:
    print("Estás desaprobado")
else:
    print("Estás aprobado")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
par=int(input("Ingresa un número par: "))
if par % 2==0:
    print("Ha ingresado un número par")
else:
    print("Ingresa un número par")
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
edad1=int(input("Ingresa tu edad: "))
if edad1 < 12:
    print("Eres un niño")
elif 12 >= edad1< 18:
    print("Eres un adolescente")
elif 18 >= edad1< 30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto")
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña=(input("Ingresa una contraseña entre 8 y 14 caracteres: "))
if 8<= len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña entre 8 y 14 caracteres")
#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma:
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")
if media > mediana > moda:
    print("Tu sesgo es positivo")
elif media < mediana< moda:
    print("Tu sesgo es negativo")
else:
    print("Sin sesgo")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase=input("Escribe una frase: ")
vocales=("a", "e", "i", "o", "u")
if frase.endswith(vocales):
    print(f"{frase}!")
else:
    print({frase})
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre=input("Dime tu nombre: ")
print("Elije una opción: \n1 MAYÚSCULAS. \n2 minúsculas. \n3 Primera letra en mayúscula")
opcion=input("Opción seleccionada: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
terremoto=float(input("Dime la magnitud de un terremoto para evaluarlo: "))
if terremoto < 3:
    print("Muy leve (Imperceptible).")
elif 3<= terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4<= terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5<= terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6<= terremoto < 7:
    print("Muy fuerte(puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio=input("Dime en cual hemisferio te encuentras (N/S): ").upper()
mes=int(input("En que mes te encuentras (1-12): "))
dia=int(input("En que día te encuentras: "))
estacion=""
if (mes==12 and dia >= 21) or mes==1 or mes==2 or (mes==3 and dia <= 20):
    estacion_norte=("Es invierno")
    estacion_sur=("Es verano")
elif (mes==3 and dia >= 21) or mes==4 or mes==5 or (mes==6 and dia <= 20):
    estacion_norte=("Es primavera")
    estacion_sur=("Es otoño")
elif (mes==6 and dia >= 21) or mes==7 or mes==8 or (mes==9 and dia <= 20):
    estacion_norte=("Es verano")
    estacion_sur=("Es invierno")
elif(mes==9 and dia >=21) or mes==10 or mes==11 or (mes==12 and dia <=20):
    estacion_norte=("Es otoño")
    estacion_sur=("Es primavera")
if hemisferio== "N":
    estacion=estacion_norte
elif hemisferio== "S":
    estacion=estacion_sur
else:
    "Elige un hemisferio válido"
print(f"{estacion}")