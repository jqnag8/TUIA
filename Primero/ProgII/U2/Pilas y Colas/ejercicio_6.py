class Nodo:
    def __init__(self, dato: any) -> None:
        self.dato = dato
        self.prox = None
    
class Qeue:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self) -> bool:
        """Verifica si la cola está vacía"""
        return self.length == 0

    def insert(self, dato: any):
        """Agrega un dato nuevo a la cola"""
        nodo = Nodo(dato)

        if self.isEmpty():
            self.head = self.last = nodo
        else:
            self.last.prox = nodo
            self.last = nodo

        self.length += 1

    def remove(self, index: int):
        """Remuve el dato en la posicion 'index'. Se asume que tiene datos"""
        dato = self.head.dato
        self.head = self.head.prox
        self.length -= 1

        return dato
        
