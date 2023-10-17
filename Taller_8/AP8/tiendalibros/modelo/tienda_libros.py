from carro_compra import CarroCompras
from libro import Libro
class TiendaLibros:
    pass
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompra()

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn, titulo)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, isbn, cantidad):
        libro = self.catalogo.get(isbn)
        if libro is None:
            raise LibroError(f"No existe un libro con el ISBN {isbn}")

        if libro.existencias == 0:
            raise LibroAgotadoError(isbn, libro.titulo)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(isbn, libro.titulo, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)
    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)




    

   

   

   

    