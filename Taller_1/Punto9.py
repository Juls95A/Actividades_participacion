#Crear un programa que genere una matriz de números y la imprima en pantalla.
 
filas=3
columnas=3

matriz=[[fila*columnas+columna+1 for columna in range(columnas)]for fila in range(filas)]
for fila in matriz:
    print(fila)
    