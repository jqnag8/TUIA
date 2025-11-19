from typing import Any


class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

class BSTree(Tree):
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        super().__init__(cargo, left, right)

    def buscar(self, elemento: Any) -> bool:
        """Verifica si un elemento está en el árbol"""

        if self.cargo == elemento:
            return True

        if self.left is not None:
            self.left.buscar()

        if self.right is not None:
            self.right.buscar()
            
        return False

    def menor_mayor(self) -> tuple(Any, Any):
        """Retorna el menor y mayor elemento del árbol"""

        minimo: BSTree = self.left
        maximo: BSTree = self.right

        while minimo.left is not None:
            minimo = minimo.left

        while maximo.right is not None:
            maximo = maximo.right

        return (minimo, maximo)

    def insertBST(self, tree_1: 'BSTree') -> None:
        """Inserta un arbol en el arbol binario de busqueda"""

        if tree_1.cargo < self.cargo:
            if self.left is None:
                self.left = tree_1
            else:
                self.left.insertBST(tree_1)

        if tree_1.cargo > self.cargo:
            if self.right is None:
                self.right = tree_1
            else:
                self.right.insertBST(tree_1)

        return None


    
