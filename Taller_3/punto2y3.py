#Cree una clase Punto que represente un punto en el plano cartesiano.

#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

import math

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mostrar_coordenadas(self):
        print("Coordenadas X:",self.x)
        print("Coordenadas Y:",self.y)
        
p1=Punto()
print(p1.mostrar_coordenadas())



def mover(self,n_x,n_y):
    self.x=n_x
    self.y=n_y

def calcular_distancia(self, otro_punto):
    distancia = ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5

p2=Punto()
print(p2.calcular_distancia())



