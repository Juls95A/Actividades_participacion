from reglas_validacion import ReglaValidacion, ReglaValidacionGanimedes, ReglaValidacionCalisto

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
