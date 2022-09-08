"""Cree un diccionario que contenga el nombre de una ciudad, el país al que pertenece y la cantidad de habitantes que tiene. Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
 Agregar ciudades
 Eliminar ciudades
 Indicar la cantidad de habitantes en un país en particular
 El porcentaje de habitantes en una ciudad de acuerdo al total registrado"""
from calendar import c

lista1=[]
lista=[]
ciudades={"Berlin":["Alemania", 100], "Mendoza":["Argentina", 10]}
while True:
    
    desicion=int(input("\n\n 1) Agregar ciudades\n 2) Eliminar ciudades \n 3) Conocer cantidad de habitantes de una ciudad \n 4) Porcentaje de habitantes en relacion en relacion a todas las ciudades\n\n Elija una opción: "))
    
    if desicion==1:
        ciudad=input("Ingrese ciudad que quiere agregar: ")
        pais=input("Ingrese pais al que pertence la ciudad: ")
        habitantes=int(input("Ingrese cantidad de habitantes: "))
        ciudades[ciudad]=[pais,habitantes]
        print(ciudades)       
        continue
        
    if desicion==2:
        borrar=input("Ingrese ciudad a eliminar: ")
        del ciudades[borrar]
        print(ciudades)
        continue
    
    if desicion==3:
        habitante=input("ingrese ciudad para saber su cantidad de habitantes: ")
        lista=ciudades[habitante]
        print(f"La cantidad de habitantes de {habitante} es: {lista[1]}")
        
    if desicion==4:
        for i in ciudades.values():
            lista.append(i)
        for i in range(len(lista)):
            lista1.append(lista[i][1])
    print(sum(lista1))
  
        
    