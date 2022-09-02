"""Se ha establecido un programa para estimular a los alumnos,
el cual consiste en lo siguiente: si el promedio global obtenido
por un alumno en el último periodo es mayor o igual que 4, se le
hará un descuento del 30% sobre la matrícula y no se le cobrará 
IVA; si el promedio obtenido es menor que 4 deberá pagar la
matrícula completa, la cual debe incluir el 10% de IVA. Hacer un
algoritmo que calcule el valor a pagar si se conocen las notas
finales de las 6 materias que cursaron"""

notas=[]
matricula=int(input("ingrese el valor de la matricula: "))
calificacion=int(input("ingrese la calificación: "))
notas.append(calificacion)
ingreso=input("desea seguir cargando notas?")

while ingreso=="si" or ingreso=="s" or ingreso=="SI":
    calificacion=int(input("ingrese la proxima calificación: "))
    notas.append(calificacion)
    ingreso=input("desea seguir cargando notas?")
    
prom=sum(notas)/len(notas)
if prom<4:
    print(f"no aplico a beca por tener promedio de {prom:.2f}, el valor de la matricula es: {matricula+(matricula*0.1):.0f}\nlas notas son ",notas)
else: print(f"aplico a la beca, promedio {prom:.2f}, valor de la matricula: {matricula-(matricula*0.3):.0f}\nlas notas son ",notas)