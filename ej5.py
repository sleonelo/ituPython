"""Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo
que éstos se calculan en base a las horas semanales trabajadas y de acuerdo a un
precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas
extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria."""

horasSemanales=int(input("ingrese las horas trabajadas por el empleado: "))
cuantoCobra=int(input("cuanto cobra ese empleado por hora? "))
if horasSemanales<=40:
    print(horasSemanales*cuantoCobra)
else: print("el empleado debe cobrar: ", 40*cuantoCobra+(horasSemanales-40)*(cuantoCobra*1.5))