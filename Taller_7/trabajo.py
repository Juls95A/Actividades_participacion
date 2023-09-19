class Elemento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elem == elemento for elem in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elem in otro_conjunto.elementos:
            self.agregar_elemento(elem)

    def __add__(self, otro_conjunto):
        new_conjunto = Conjunto(self.elementos.copy(), self.nombre)
        new_conjunto.unir(otro_conjunto)
        return new_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        interseccion_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        interseccion_elementos = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        return Conjunto(interseccion_elementos, interseccion_nombre)

    def __str__(self):
        nombres_elementos = ', '.join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({nombres_elementos})"
