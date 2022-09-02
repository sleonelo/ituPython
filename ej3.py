valor=int(input("ingrese un numero para saber todos los multiplos de 5 que tiene: "))
for x in range(1,valor):
    if x%5==0:
        print(f"son multiplos de 5: {x}")
    