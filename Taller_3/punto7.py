#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.

class CuentaBancaria:
    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("1234567890", ["Sara", "Gustavo"], 1000.0)
    print("Número de cuenta:",cuenta1.numero_cuenta)
    print("Propietarios:",cuenta1.propietarios)
    print("Balance:",cuenta1.balance,"USD")