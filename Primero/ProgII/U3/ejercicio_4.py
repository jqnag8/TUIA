from typing import Any


class Tree:
    def __init__(self, cargo: Any, left = None, right = None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right


def copiar(tree_1: Tree) -> Tree:
    resultado = Tree(tree_1.cargo, tree_1.left, tree_1.right)

    return resultado

