from typing import Any


class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

class BSTree(Tree):
    def __init__(self, cargo: Any, left = None, right = None) -> None:
        super().__init__(cargo, left, right)

    def insertBST(self, elemento: Any) -> None:
        """Inserta un arbol en el arbol binario de busqueda"""

        if elemento < self.cargo:
            if self.left is None:
                self.left = BSTree(elemento)
            else:
                self.left.insertBST(elemento)

        if elemento > self.cargo:
            if self.right is None:
                self.right = BSTree(elemento)
            else:
                self.right.insertBST(elemento)

        return None

# Funciones -----
def listar_elementos(tree_1: BSTree) -> list[Any]:
    """Recorre los elementos de un arbol de forma transversal"""
    if tree_1 is None:
        return []
    else:
        return listar_elementos(tree_1.left) + [tree_1.cargo] + listar_elementos(tree_1.right)

def combinar(tree_1: BSTree, tree_2: BSTree) -> BSTree:
    """Recorre el 'tree_2' en la forma InOrder y agrega los elementos a 'tree_1'"""
    resultado: BSTree = BSTree(tree_1.cargo, tree_1.left, tree_1.right)
    lista_elementos = listar_elementos(tree_2)

    for elemento in lista_elementos:
        resultado.insertBST(elemento)

    return resultado
    
