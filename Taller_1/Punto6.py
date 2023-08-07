#Crear un programa que calcule la suma de los números en una lista dada.

n= int(input("Usuario por favor Ingrese los numeros"))

lista= [float(input("Ingrese el numero:"))for i in range (3)]
suma=0
for numero in lista:
    suma+= numero
print("La suma de los numeros en la lista es:",suma)