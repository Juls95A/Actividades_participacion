#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self,vehiculo_maxima,kilometraje):
        self.vehiculo_maxima=vehiculo_maxima
        self.kilometraje=kilometraje

mi_carro=Vehiculo()
print(mi_carro.vehiculo_maxima)
print(mi_carro.kilometraje)
