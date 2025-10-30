class Cola:
    def __init__(self) -> None:
        self.items = []

    def insert(self, dato: any) -> None:
        """Agrega el dato en la última posición"""

        self.items.append(dato)

    def remove(self) -> any:
        """Remueve el primer elemento de la cola y lo retorna"""

        if self.is_empty():
            print("Cola vacía")

        self.items.pop(0)

    def is_empty(self) -> bool:
        """Verifica si una cola está vacía"""
        return self.items == list()



    
