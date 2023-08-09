#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print("Se ha depositado",monto,"USD en la cuenta.")
        else:
            print("El monto del depósito debe ser mayor que cero.")

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("1234567890", ["Sara", "Gustavo"], 1000.0)
    print("Número de cuenta:",cuenta1.numero_cuenta)
    print("Propietarios:",cuenta1.propietarios)
    print("Balance inicial:",cuenta1.balance,"USD")
    cuenta1.depositar(500.0)
    print("Balance después del depósito:",cuenta1.balance,"USD")