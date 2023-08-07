#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

numeros=[20,43,11,37,9,34]

mayor= numeros[0]
menor=numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor= numero
    if numero<menor:
        menor=numero

print("El numero mas grande es:",mayor)
print("El numero mas pequeño es:",menor)