from typing import Any


class Tree:
    def __init__(self, cargo: Any, left = None, right = None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

    def altura(self) -> int:
        """
            Calcula la altura del árbol
        """
        altura_izq: int = 1
        altura_der: int = 1

        if self.left:
            altura_izq += self.left.altura()
        if self.right:
            altura_der += self.right.altura()

        return max(altura_izq, altura_der)


def sumatoria_rango(tree_1: Tree, M: int) -> int | None:
    """Calcula la suma de todos los
    números del árbol que se encuentren entre inicio y final, a lo sumo hasta
    el nivel 'M'"""
    resultado: int = tree_1.cargo
    altura: int = tree_1.altura()

    if altura < M:
        return None

    if altura > altura - (M - 1): # M indica cuantas veces se ejecuta la recursion
        if tree_1.left is not None:
            resultado += sumatoria_rango(tree_1.left, M - 1)

        if tree_1.right is not None:
            resultado += sumatoria_rango(tree_1.right, M - 1)

    return resultado 



# TEST
def test_sumatoria_rango():
    nodo_4 = Tree(4)
    nodo_5 = Tree(5)
    nodo_6 = Tree(6)
    nodo_7 = Tree(7)

    nodo_2 = Tree(2, left=nodo_4, right=nodo_5)

    nodo_3 = Tree(3, left=nodo_6, right=nodo_7)

    arbol_enteros = Tree(1, left=nodo_2, right=nodo_3)

    assert sumatoria_rango(arbol_enteros, 1) == 1
    assert sumatoria_rango(arbol_enteros, 2) == 6
    assert sumatoria_rango(arbol_enteros, 3) == 28
    assert sumatoria_rango(arbol_enteros, 4) is None

