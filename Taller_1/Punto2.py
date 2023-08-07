#Escribir una función que calcule el área de un círculo dado su radio.

import math

def area_circulo(radio):
    area=math.pi*radio**2
    return area

radio_circulo=float(input("Por favor ingrese el radio"))
area_del_circulo=area_circulo(radio_circulo)
print("El area del circulo es ",area_del_circulo)
    
