"""Leer una secuencia de números y determinar el mayor de los pares leídos."""
pares=[]
numeros=[]
num=int(input("ingrese un numero: "))
numeros.append(num)
desicion=str(input("desea seguir ingresando numeros? "))
while desicion=="s" or desicion=="si" or desicion=="SI" or desicion=="S":
    num=int(input("ingrese otro numero: "))
    numeros.append(num)
    desicion=str(input("desea seguir ingresando numeros? "))

for i in numeros:
    if i%2==0:
       pares.append(i)
print(f"El numero par mas alto es: {max(pares)}")

