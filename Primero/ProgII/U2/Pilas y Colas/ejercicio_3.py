from typing import Any

class Pila:
    def __init__(self):
        self.items = []

    def push(self, x: Any):
        self.items.append(x)

    def pop(self) -> Any | None:
        if self.is_empty():
            print("Está vacía")
            return None
        else:
            return self.items.pop()

    def is_empty(self) -> bool:
        return self.items == []

    def mostrar_Pila(self) -> None:
        for elem in self.items:
            print(elem)


class PilaConMaximo(Pila):
    def __init__(self):
        super().__init__()
        self.maximos = Pila()

    def push(self, dato: Any) -> None:
        """Ingresa el dato a la cola y verifica que no sea maximo"""
        super().push(dato)

        if self.maximos.is_empty():
            self.maximos.push(dato)

        if self.maximos.items[0] < dato:
            self.maximos.push(dato)

    def pop(self) -> None:
        """Elimina el dato de la lista y de los maximos en caso de que lo haya sido"""
        if self.items[-1] == self.maximos.items[-1]:
            self.maximos.pop()

        super().pop()

    def obtener_maximo(self) -> None:
        return self.maximos.items[-1]
     
