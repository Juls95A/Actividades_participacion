
#Escribir una función que calcule el factorial de un número dado.
#(Formula factorial = n ( n − 1 ) ! )

def factorial(numero):
    resultado=1
    for i in range(1,numero+1):
        resultado *= i
    return resultado

numero= int(input("Ingresa un numero"))
resultado= factorial(numero)
print("El factorial del numero es:", resultado)