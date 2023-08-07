#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla

from random import randint

numero_random= [randint(1,100)for i in range(10)]

print(numero_random)
