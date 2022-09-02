numeros=int(input("ingrese un numero: "))
mayor=0
while numeros>0:
    numeros=int(input("ingrese otro numero: "))
    if numeros%2==0 and numeros>mayor:
        mayor=numeros
            
print(mayor)
        