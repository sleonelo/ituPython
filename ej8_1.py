"""Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
Finalizar al ingresar el número 0, el cual no debe guardarse. Luego de que se termina
la carga de la lista, solicitar al usuario otro número y crear una lista con los 
elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""
numeros1=[]
numeros=[]

num=int(input("ingrese numeros: "))
numeros.append(num)
while num!=0:
    num=int(input("ingrese otro numero: "))
    numeros.append(num)
    
    
num1=int(input("ingrese el ultimo numero: "))
for x in numeros:
    if x<num1:
        numeros1.append(x)

numeros1.remove(0)
print(numeros1)