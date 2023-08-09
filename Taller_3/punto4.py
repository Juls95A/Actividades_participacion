#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def imprimir_perimetro(self):
        print("Perímetro:", 2 * (self.ancho + self.altura))

    def imprimir_area(self):
        print("Área:", self.ancho * self.altura)

    def es_cuadrado(self):
        if self.ancho == self.altura:
            print("Es un cuadrado.")
        else:
            print("No es un cuadrado.")

mi_rectangulo=Rectangulo()

print(mi_rectangulo.imprimir_perimetro())
print(mi_rectangulo.imprimir_area())

    
