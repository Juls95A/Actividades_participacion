from abc import ABC, abstractmethod
from errores import LongitudInvalidaError, MayusculaInvalidaError, MinusculaInvalidaError, NumeroInvalidoError, CaracterEspecialInvalidoError, CalistoInvalidoError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) >= self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        return any(caracter in clave for caracter in caracteres_especiales)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError("La longitud de la clave es inválida")

        if not self._contiene_mayuscula(clave):
            raise MayusculaInvalidaError("La clave no contiene una letra mayúscula")

        if not self._contiene_minuscula(clave):
            raise MinusculaInvalidaError("La clave no contiene una letra minúscula")

        if not self._contiene_numero(clave):
            raise NumeroInvalidoError("La clave no contiene un número")

        if not self.contiene_caracter_especial(clave):
            raise CaracterEspecialInvalidoError("La clave no contiene un carácter especial")

        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        return 'CALISTO' in clave and any(c.isupper() for c in 'CALISTO') and not all(c.isupper() for c in 'CALISTO')

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError("La longitud de la clave es inválida")

        if not self._contiene_mayuscula(clave):
            raise MayusculaInvalidaError("La clave no contiene una letra mayúscula")

        if not self._contiene_minuscula(clave):
            raise MinusculaInvalidaError("La clave no contiene una letra minúscula")

        if not self._contiene_numero(clave):
            raise NumeroInvalidoError("La clave no contiene un número")

        if not self.contiene_calisto(clave):
            raise CalistoInvalidoError("La clave no cumple con las reglas de Calisto")

        return True

