from typing import Any

class Grafo:
    def __init__(self):
        self.vertices: set[Any] = set()
        self.vecinos: dict[Any, set[tuple[Any, Any]]] = dict()
   
    # Metodo __eq__
    def __eq__(self, other: 'Grafo'):
        """Compara dos grafos"""
        return self.vertices == other.vertices and self.vecinos == other.vecinos
    
    
