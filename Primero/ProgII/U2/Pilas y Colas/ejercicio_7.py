class Cliente:
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas

class ColaGeneralizada():
    def __init__(self) -> None:
        self.items = []

    def push(self, cliente: Cliente) -> None:
        """ingresa un cliente a la cola"""
        self.items.append(cliente)

    def remove(self) -> None:
        """Elimina el primer elemento de la ColaGeneralizada"""

        cliente_atendido = self.items[0]

        if cliente_atendido.cant_cartas > 5:
            print(f"Atendido cliente {cliente_atendido.nombre}, despachadas 5 cartas")
            cliente_mod = Cliente(cliente_atendido.nombre, cliente_atendido.cant_cartas - 5)
            self.push(cliente_mod)
        else:
            print(f"Atendido cliente {cliente_atendido.nombre}, despachadas {cliente_atendido.cant_cartas} cartas")

        self.items.pop(0)

    def is_empty(self) -> None:
        return self.items == list()
