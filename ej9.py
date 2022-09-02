"""Leer una secuencia de 10 números, almacenarlos en una lista y mostrar la suma de los elementos que
ocupan posiciones pares y el mayor número de los que ocupan posiciones impares."""
num1=[]
num=[]
num2=[]
numeros=int(input("ingrese un numero: "))
num.append(numeros)

while len(num)<10:
   numeros=int(input("ingrese otro numero: "))
   num.append(numeros)
     
for i in range(0,len(num)):
   if i%2!=0:
      num1.append(num[i])
      
print("suma de posiciones pares: \n",sum(num1))

for i in range(0,len(num)):
   if i%2==0:
      num2.append(num[i])
      
print("mayor numero de posicion impar: \n",max(num2))

