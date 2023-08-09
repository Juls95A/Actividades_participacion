#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

class Circulo:
    def __init__(self,centro,radio):
        self.centro_x=centro
        self.centro_y=centro
        self.radio=radio
    
    def calcular_area(self):
        self.area=3.14*self.radio**2
    
    def calcular_perimetro(self):
        self.perimero=2*3.14*self.radio

    def punto_pertenece(self,x,y):
        self.pertenece=(x - centro_x)^2 + (y - centro_y)^2 <= radio^2
        if pertenece:
            print("El punto pertenece")
        else:
            ("El punto no pertenece")