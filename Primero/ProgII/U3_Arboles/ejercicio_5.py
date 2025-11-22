from typing import Any


class Tree:
    def __init__(self, cargo: Any, left = None, right = None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

    def Pre_Order(self) -> None:
        """Realiza un recorrido Pre Order por el árbol"""
        sl = self.left
        sr = self.right

        print(self.cargo)

        if sl is not None:
            sl.Pre_Order()

        if sr is not None:
            sr.Pre_Order()


def invertir(tree_1: Tree) -> None:
    """Invierte de lugar todos los nodos del arbol"""

    if tree_1.left is not None and tree_1.right is not None:
        tree_1.left, tree_1.right = tree_1.right, tree_1.left 

    if tree_1.left is not None:
        invertir(tree_1.left)

    if tree_1.right is not None:
        invertir(tree_1.right)

    return None

    
    
