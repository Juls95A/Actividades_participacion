from tiendalibros.modelo.item_compra import ItemCompra
from tiendalibros.modelo.libro import Libro

class CarroCompras:
    pass
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.items:list[ItemCompra]=[]

    # Defina el metodo agregar_item
    def agregar_item(self, libro:Libro, cantidad:int):
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item
    

    # Defina el metodo calcular_total
    
    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total
    
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]


     

    


    