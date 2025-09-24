class Billetera:

    def __init__(self, id_cuenta: int, saldo: float = 0):
        self.id_cuenta = id_cuenta
        self.saldo = saldo
        self.porcentaje_de_reintegro: float = 30
        self.monto_maximo_de_reintegro: float = 5000

    def acreditar(self, monto_ing: float) -> None:
        """
            Ingresa un monto al saldo de la cuenta
        """
        self.saldo += monto_ing

    def pagar(self, monto_pagar: float) -> None:
        """
            Resta el dinero que hay en saldo aplicando el porcentaje correspondiente
        """
        if monto_pagar > self.saldo:
            print("No hay saldo suficiente para pagar")
            return None

        descuento: float = (monto_pagar * 30) / 100

        if descuento > self.monto_maximo_de_reintegro:
            descuento = self.monto_maximo_de_reintegro
            
        self.monto_maximo_de_reintegro -= descuento
        self.saldo -= (monto_pagar - descuento)

    def monto_descuento_pendiente(self):
        """
            Retorna el monto restante del descuento
        """
        return self.monto_maximo_de_reintegro    
