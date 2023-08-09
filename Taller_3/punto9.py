#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance,saldo):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        self.saldo=saldo


    def depositar(self, monto):
            self.balance += monto
            print("Se ha depositado",monto,"USD en la cuenta.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            print("Se ha retirado",monto,"USD de la cuenta.")

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("1234567890", ["Sara", "Gustavo"], 1000.0)
    print("Número de cuenta:",cuenta1.numero_cuenta)
    print("Propietarios:",cuenta1.propietarios)
    print("Balance inicial:",cuenta1.balance,"USD")
    cuenta1.depositar(500.0)
    print("Balance después del depósito:",cuenta1.balance,"USD")
    cuenta1.retirar(300.0)
    print("Balance después del retiro:",cuenta1.balance,"USD")