import math
#1) 
def hola_mundo():
    print("Hola Mundo!")
hola_mundo()

#2)
def saludo(nombre):
    return f"Hola {nombre}"
nombre_usuario = input("Ingresa tu nombre: ")
print(saludo(nombre_usuario))

#3)
def  informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nom= input("Ingresa tu nombre: ")
apelli=input("Ingresa tu apellido: ")
ed=input("Ingresa tu edad: ")
residen=input("Ingresa tu residencia: ")
print (informacion_personal(nom,apelli,ed,residen))

#4)
def calcular_area_circulo(radio):
    return math.pi * radio
rad=float(input(f"Ingresa el radio de un circulo para calcular su area: "))
print(calcular_area_circulo(rad))

#5)
def segundos_a_horas(segundos):
    return segundos / 3600
seg=int(input("Ingresa la cantidad de segundos que quieres convertir a horas: "))
print(segundos_a_horas(seg))

#6)
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}")
    for i in range (1,11):
        print(f"{numero * i}")
num= int(input("Ingresa el numero con el que quieras hacer una tabla de multiplicacion: "))
print(tabla_multiplicar(num))

#7)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
numero1= int(input("Ingresa el primer numero: "))
numero2= int(input("Ingresa el segundo numero: "))
print(f"Las operaciones de tus numeros son (suma,resta,multiplicacion,division):", (operaciones_basicas(numero1,numero2)))

#8)
def  calcular_imc(peso, altura):
    return peso / (altura**2)
pes=float(input("Di tu peso: "))
alt=float(input("Di tu altura: "))
print("IMC: "(calcular_imc(pes,alt)))

#9)
def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32
grados=int(input("Di los grados celsius que quieras para pasarlos a grados fahrenheit: "))
print(celsius_a_fahrenheit(grados))

#10)
def calcular_promedio(a, b, c):
    return (a+b+c) / 3
num1=int(input("Di el primer numero: "))
num2=int(input("Di el segundo numero: "))
num3=int(input("Di el tercer numero: "))
print(f"El promedio de tus numeros es: ", (calcular_promedio(num1,num2,num3)))