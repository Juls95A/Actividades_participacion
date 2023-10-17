from tiendalibros.modelo.libro import Libro
from libro import precio


class ItemCompra:
   def __init__(self, libro:Libro, cantidad:int):
        self.libro = libro
        self.cantidad = cantidad
    
    def calcular_subtotal(self):
        return self.cantidad * self.libro.precio

