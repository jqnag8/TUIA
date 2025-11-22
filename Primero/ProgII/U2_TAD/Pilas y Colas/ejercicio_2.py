class _Nodo:
    def __init__(self, dato: any):
        self.dato = dato
        self.prox = None

    
class PilaEnlazada:
    def __init__(self):
        self.tope = None

    def push(self, x):
        nodo = _Nodo(x)

        if not self.is_empty():
            nodo.prox = self.tope

        self.tope = nodo

    def pop(self, x):
        if self.is_empty():
            print("Está vacía")
            return None
        else:
            nodo = self.tope.dato
            self.tope = self.tope.prox
            return nodo.dato

    def is_empty(self):
        return self.tope is None

    def mostrar_pila(self) -> None:
        nodo = self.tope

        while nodo.prox is not None:
            print(self.tope.dato)
            nodo = nodo.prox

        return None

