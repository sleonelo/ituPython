# -*- coding: utf-8 -*-

"""Escribir un programa que pregunte al usuario una cantidad de dinero ($) a invertir,
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión. Nota: el valor inicial de cada año depende 
del capital + interés obtenido en el año anterior."""

anual=int(0)
dinero=int(input("ingrese el dinero a invertir: "))
interes=int(input("ingrese el interes que desea: "))
anios=int(input("ingrese la cantidad de años de la inversion: "))
capital=int(((dinero*interes)/100)*anios)
for i in range(0,anios):
        anual+=(capital/anios)
        print(f"capital del año {i+1} \n {round(anual)}")
        