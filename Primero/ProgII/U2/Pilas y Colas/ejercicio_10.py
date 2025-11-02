from typing import Any

class Cola:
    def __init__(self) -> None:
        self.items = []

    def insert(self, dato: any) -> None:
        """Agrega el dato en la última posición"""

        self.items.append(dato)

    def remove(self) -> Any:
        """Remueve el primer elemento de la cola y lo retorna"""

        if self.is_empty():
            print("Cola vacía")

        return self.items.pop(0)

    def is_empty(self) -> bool:
        """Verifica si una cola está vacía"""
        return self.items == list()

class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, codigo: str) -> None:
        """Inserta el codigo de un nuevo arribo en el stack arribos"""
        self.arribos.insert(codigo)

    def nueva_partida(self, codigo: str) -> None:
        """Inserta el codigo de una nueva partida en el stack partidas"""
        self.partidas.insert(codigo)

    def asignar_pista(self) -> None:
        """
            Aterriza o despega aviones segun la prioridad.
        """
        sa = self.arribos
        sp = self.partidas

        if sa.is_empty and sp.is_empty:
            print("No hay vuelos en espera")
        elif not sa.is_empty():
            print(f"El vuelo {sa.remove()} aterrizó con éxito")
            return
        else:
            print(f"El vuelo {sp.remove()} despegó con éxito")

        
    def mostrar_estado(self) -> None:
        """Muestra el estado de la torre de control, si existen partidas o arribos"""
        sa = self.arribos
        sp = self.partidas

        if sa.items != []:
            print("Hay vuelos esperando para aterrizar.")

        if sp.items != []:
            print("Hay vuelos esperando para despegar.")
