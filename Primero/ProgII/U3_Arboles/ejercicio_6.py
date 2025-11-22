from typing import Any


class Tree:
    def __init__(self, cargo: Any, left = None, right = None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right


def sumatoria(tree_1: Tree) -> int:
    resultado: int = tree_1.cargo

    if tree_1.left is not None:
        resultado += sumatoria(tree_1.left)

    if tree_1.right is not None:
        resultado += sumatoria(tree_1.right)

    return resultado


    
  
