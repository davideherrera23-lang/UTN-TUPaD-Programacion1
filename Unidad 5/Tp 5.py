#1)

multiplos_de_cuatro = list(range(1,101,4))
print(f"Los multiplos de 4 son: {multiplos_de_cuatro}")

#2)

objetos = [ "Guitarra", "Flauta", "Teclado", 'Piano', 'Arpa']
penultimo=objetos[-2]
print(f"El penultimo objeto es: {penultimo}")

#3)

lista_vacia = []
lista_vacia.append('Perro')
lista_vacia.append('Lagarto')
lista_vacia.append('Gato')
print(f'{lista_vacia}')

#4)

animales=['perro','gato','conejo','pez']
animales[1]= 'loro'
animales[3]= 'oso'
print(animales)

#5)El programa elimina al numero mas grande de la lista

#6)

lista_numeros= list(range(10,31,5))
dos_numeros= lista_numeros[0:2]
print(dos_numeros)

#7)

autos = ["sedan", "polo", "suran", "gol"]
autos[1]= 'bugatti'
autos[2]= 'bmw'
print(autos)
#8)

dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append('jugo')
compras[1][1]= "tallarines"
compras[0].remove("pan")
print(compras)

#10)

lista_anidada=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada)