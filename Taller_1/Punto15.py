#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no

print ("Hola Usuario")
texto= input("Ingrese un texto:")
texto=texto.lower().replace("","")

if texto == texto[::-1]:
    print("Es un palindromo")
else:
    print("No es palindromo")
