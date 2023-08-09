#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta

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

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print("Se ha retirado",monto,"USD de la cuenta.")
        else:
            print("El monto del retiro debe ser mayor que cero y no exceder el balance disponible.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2%: {cuota_manejo} USD")

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("1234567890", ["Sara", "Gustavo"], 1000.0)
    print("Número de cuenta:",cuenta1.numero_cuenta)
    print("Propietarios:",cuenta1.propietarios)
    print("Balance inicial:",cuenta1.balance,"USD")
    cuenta1.depositar(500.0)
    print("Balance después del depósito:", cuenta1.balance,"USD")
    cuenta1.aplicar_cuota_manejo()
    print("Balance después de la cuota de manejo:",cuenta1.balance,"USD")
