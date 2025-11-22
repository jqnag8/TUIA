from typing import Any

class Grafo:
    def __init__(self) -> None:
        self.vertices: set[Any] = set()
        self.vecinos: dict[Any, set[Any]] = dict()

    def add_node(self, vertice: Any) -> None:
        self.vertices.add(vertice)
        self.vecinos[vertice] = set()

    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
        self.vecinos[vertice1].add(vertice2)
        self.vecinos[vertice2].add(vertice1)

    def get_adjacent(self, vertice: Any) -> set | None:
        if vertice not in self.vecinos:
            print("Nodo no encontrado")
            return None

        return self.vecinos[vertice]
    
    def get_nodes(self) -> set[Any]:
        return self.vertices

    def remove_node(self, x: Any):
        """Remueve un nodo dentro de un grafo no directo"""
        if x not in self.vertices:
            print("El nodo no se encuentra")
        
        for vecino in self.vecinos[x]:
            self.vecinos[vecino].discard(x)
        
        del self.vecinos[x]
        self.vertices.discard(x)

    def are_adjacent(self, x: Any, y: Any):
        """"Retorna True si 'x' e 'y' son adyacentes"""
        if x in self.vecinos[y] and y in self.vecinos[x]:
            return True
        
        return False
    
    def is_node(self, x: Any):
        """Verifica si x es un nodo"""
        return x in self.vertices

    # Metodo __eq__
    def __eq__(self, other: 'Grafo'):
        """Compara dos grafos"""
        return self.vertices == other.vertices and self.vecinos == other.vecinos

    
