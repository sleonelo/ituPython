"""Dado una lista de 10 nombres de personas, realice un programa que cargue la lista,
la ordene de forma ascendente y la muestre por pantalla ordenado. Python nos brinda la
función “sorted” para realizar dicho procedimiento, pero la idea es que el ejercicio se
resuelva utilizando algoritmia propia de algún método de ordenamiento existente."""

lista=["alfa","bravo","charly","juliet","delta","eco","foxtrot","golf","hotel","india","loro", "jorge"]
            
def ordenar_alfabeticamente(lista):
    alfabeto="abcdefghijklmnñopqrstuvwxyz"
    for i in range(1,len(lista)):
        actual=alfabeto.index(lista[i][0])
        palabra_actual=lista[i]
        indice=i
        while indice>0 and alfabeto.index(lista[indice-1][0])>actual:
            lista[indice]=lista[indice-1]
            indice=indice-1
        lista[indice]=palabra_actual
    print(lista)


ordenar_alfabeticamente(lista)