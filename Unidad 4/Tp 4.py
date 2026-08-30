#1)

for i in range (101):
   print(i)

#2)

numeros=str(input("Pon un número para sacar sus dígitos: "))
print(len(numeros))

#3)

inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los números es: {suma}")

#4)

suma2= 0
numero=-1
while numero != 0:
    numero=int(input("Ingresa un número: "))
    suma2+=numero
print(f"La suma de los números es:{suma2}" )

#5)

import random
numero1=random.randint(0,9)
adivinar=int(input("Adivina un número del 0 al 9: "))
intentos=0
adivinado=False
while not adivinado:
    intentos_persona=int(input("Fallaste, dí otro número: "))
    intentos+=1
    if intentos_persona == numero1:
        print("Felicidades, adivinaste.")
        print(f"Tu cantidad de intentos fueron: {intentos}")
        adivinado=True

#6)

for i in range (100,-1, -2):
    print(i)

#7)

numero=int(input("Dí un número: "))
suma=0
for i in range(numero+1):
    suma+= i
    print(f"Tu suma es: {suma}")

#8)

impar=0
par=0
negativo=0
positivo=0
total=100
num=int(input(f"Dime {total} números: "))
for i in range(total):
    num=int(input("ingresa un número:"))
    if num % 2 ==0:
        par+=1
    else:
        impar+=1
    if num <0:
        negativo+=1
    else:
        positivo+=1
print("Resultados:")
print(f"pares: {par}")
print(f"impares. {impar}")
print(f"negativos: {negativo}")
print(f"positvos: {positivo}")

#9)

total=100
suma=0
num=print(f"Dime {total} números: ")
for i in range(total):
    num=int(input("Ingresa un número: "))
    suma=suma+num
media=suma/total
print(f"La media total es: {media}")

#10

numero=input("Ingresa un número: ")
invertido= numero[::-1]
print(f"Tu número invertido es: {invertido}")
