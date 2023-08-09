#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
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
            print(f"Se ha retirado",monto,"USD en la cuenta.")
        else:
            print("El monto del retiro debe ser mayor que cero y no exceder el balance disponible.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2%: {cuota_manejo} USD")

    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance} USD")

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("1234567890", ["Sara", "Gustavo"], 1000.0)
    cuenta1.mostrar_detalles()
    cuenta1.depositar(500.0)
    cuenta1.mostrar_detalles()
    cuenta1.aplicar_cuota_manejo()
    cuenta1.mostrar_detalles()