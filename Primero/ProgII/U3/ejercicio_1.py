from typing import Any


class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right


tree_1 = Tree(4)
tree_2 = Tree(1, Tree(3), Tree(2))
tree_3 = Tree(1, Tree(3), Tree(2))
tree_4 = Tree(None)
