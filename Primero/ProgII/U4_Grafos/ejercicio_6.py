from typing import Any

class Grafo:
    def __init__(self):
        self.vertices: set[Any] = set()
        self.vecinos: dict[Any, set[tuple[Any, Any]]] = dict()

def is_induced_graph(G: Grafo, H: Grafo) -> bool:
    """Verifica si el grafo H es un subgrafo inducido en G"""
    for vertice in H.vertices:
        if vertice not in G.vertices:
            return False

    for vertice, vecinos in H.vecinos:
        vecinos_grafo = G.vecinos[vertice]

        for vecino in vecinos:
            if vecino not in vecinos_grafo:
                return False

    return True


# TEST
            

            
