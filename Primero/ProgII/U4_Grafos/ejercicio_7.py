from typing import Any

class Grafo:
    def __init__(self) -> None:
        self.vertices: set[Any] = set()
        self.vecinos: dict[Any, set[Any]] = dict()

def is_complete(G: Grafo) -> bool:
    """Verifica si un grafo es completo"""
    for vertice in G.vertices:
        for vertice, vecinos in G.vecinos:
            if vertice not in vecinos:
                return False

    return True


# TEST
            
