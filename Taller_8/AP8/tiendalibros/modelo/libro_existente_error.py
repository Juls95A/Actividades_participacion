from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, isbn, titulo):
        super().__init__()
        self.isbn = isbn
        self.titulo = titulo

    def __str__(self):
        return f"El libro con título {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"

class LibroAgotadoError(LibroError):
    def __init__(self, isbn, titulo):
        super().__init__()
        self.isbn = isbn
        self.titulo = titulo

    def __str__(self):
        return f"El libro con título {self.titulo} y isbn {self.isbn} está agotado"

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, isbn, titulo, cantidad_a_comprar, existencias):
        super().__init__()
        self.isbn = isbn
        self.titulo = titulo
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con título {self.titulo} y isbn {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"