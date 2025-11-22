from Typing import Any

class Stack:
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


class FastQueue:
    def __init__(self):
        self.stack_insert = Stack()
        self.stack_remove = Stack()

    def insert(self, dato: Any) -> None:
        """Inserta elementos en el stack insert"""
        self.stack_insert.append(dato)

    def pop(self) -> None:
        """Verifica si el stack_remove está vacio y si es asi, vuelva los elementos del stack instert.
        Luego, remueve el elemento"""
        sr = self.stack_remove
        si = self.stack_insert

        if sr.is_empty():
            long = len(si.items)

            for _ in range(long):
                sr.push(si.pop())

        sr.pop()
        
    def mostrar_items(self):
        """Muesta los elementos dentro del stack"""
        sr = self.stack_remove
        si = self.stack_insert

        for elemento in si.items:
            print(elemento)

        for elemento in sr.items:
            print(elemento)

    def is_empty(self) -> bool:
        sr = self.stack_remove
        si = self.stack_insert

        return sr.is_empty() and si.is_empty()
