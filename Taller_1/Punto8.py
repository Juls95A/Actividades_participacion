
#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista):
   return lista[::-1]
 
miLista=[8,6,4,2]
invertida=invertir_lista(miLista)

print("Lista Original:",miLista)
print("Lista Invertida:",invertida)
