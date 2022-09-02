"""Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
Finalizar al ingresar el número 0, el cual no debe guardarse. Luego de que se termina
la carga de la lista, solicitar al usuario otro número y crear una lista con los 
elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""
menores=[]
listaNumeros=[]

numeros=int((input("ingrese numeros a guardar: ")))
while numeros!=0:
    listaNumeros.append(numeros)
    numeros=int((input("ingrese numeros a guardar: ")))
            
comparar=int(input("ingrese un numero: "))    
for x in listaNumeros:
        if x<comparar:
            menores.append(x)
        
print(f"los numeros ordenados son {sorted(menores)}")
