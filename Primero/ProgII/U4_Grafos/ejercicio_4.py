from typing import Any

class Grafo:
    def __init__(self) -> None:
        self.vertices: set[Any] = set()
        self.vecinos: dict[set[Any]] = dict()

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


def induce(grafo_1: Grafo, conjunto_vertices: Any) -> Grafo:
    """devuelve el grafo inducido en 'grafo_1' por el conjunto U"""
    for vertice in conjunto_vertices:
        if vertice not in grafo_1.vertices:
            print("Existe un vertice en el conjunto inducido que no está en el grafo")
    
    resultado = Grafo()

    for vertice in conjunto_vertices:
        resultado.add_node(vertice)
        for vecino in grafo_1.vecinos[vertice]:
            if vecino in conjunto_vertices:
                resultado.vecinos[vertice].add(vecino)
    
    return resultado


    
        
    

