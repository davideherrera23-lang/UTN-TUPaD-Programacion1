print("Resolución del Trabajo Práctico de Secuenciales:")
print("1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”")
print("Hola Mundo!")
from math import pi
print("2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usandoel nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimirpor pantalla “Hola Marcos!”.")
print("Dime tu nombre así te doy la bienvenida")
nombre_1=input("Nombre:")
print(f"Hola {nombre_1}!")
print("3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”:")
print("Nombre:")
nombre=input()
print("Hola" + " " + nombre + " " + ",bienvenido")
print("Apellido:")
apellido=input()
print("Edad:")
edad=input()
print("Residencia:")
residencia=input()
print("Soy" + " " + nombre + " " + apellido + "," + " " + "tengo" + " " + edad + " " + "años y vivo en" + " " + residencia)
print("4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro:")
radio=float(input("Ingresa un radio para sacar el área y perímetro de un círculo: "))
area= pi * radio**2
print(f"el area es: {area}")
perímetro= 2 * pi * radio
print(f"El perímetro es: {perímetro}")
print("5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale: ")
segundos=float(input("Ingresa los segundos para ser convertidos en horas: "))
horas= segundos / 3600
print(f"Tus segundos a horas son: {horas}")
print("6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número: ")
numero=int(input("Pon tu número para poder hacer su tabla de valores: "))
for i in range(1,11):
    resultado= numero * i
    print(f"{numero} x {i} = {resultado}")
print("7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.")
numero1=int(input("Pon tu primer número: "))
numero2=int(input("Pon tu segundo número: "))
while numero1 == 0:
        input(("No puedes poner el número 0, prueba con otro: "))
while numero2 == 0:
    input(("No puedes poner el número 0, prueba con otro: "))
suma= numero1 + numero2
print(f"Su suma es: {suma}")
resta= numero1 - numero2
print(f"Su resta es: {resta}")
multi= numero1 * numero2
print(f"Su multiplicación es: {multi}")
divi= numero1 / numero2
print(f"Su división es: {divi}")
print("8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) 2")
altura=float(input("Dime tu altura: "))
peso=float(input("Dime tu peso: "))
imc= peso/ (altura ** 2)
print(f"Tu índice de masa corporal es: {imc}")
print("9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32")
tempC=int(input("Pon tus grados Celsius: "))
tempF=(9/5) * tempC + 32
print(f"Tus grados Celsius en grados Fahrenheit son: {tempF}")
print("10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números: ")
num1= float(input("Pon tu priemer número: "))
num2= float(input("Pon tu segundo número: "))
num3=float(input("Pon tu tercer número: "))
promedio= (num1 + num2 + num3) / 3
print(f"Tu promedio es: {promedio}")