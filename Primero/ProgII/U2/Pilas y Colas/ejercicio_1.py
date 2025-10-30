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
