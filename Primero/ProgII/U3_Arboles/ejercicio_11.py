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

    def Pre_Order(self) -> None:
        """Realiza un recorrido Pre Order por el árbol"""
        sl = self.left
        sr = self.right

        print(self.cargo)

        if sl is not None:
            sl.Pre_Order()

        if sr is not None:
            sr.Pre_Order()


# Funciones -----

def borra_raiz(tree_1: BSTree) -> None:
    """Elimina la raiz del arbol y la reemplaza por otra usando el metodo in order"""

    if tree_1.right is None:
        nodo_actual: BSTree = tree_1.left
        tree_1.cargo = nodo_actual.cargo
        tree_1.left = nodo_actual.left
        tree_1.right = nodo_actual.right
        breakpoint()
        return 

    nodo_actual = tree_1.right
    hist_nodos: list[BSTree] = list()

    while nodo_actual.left is not None:
        hist_nodos += [nodo_actual]
        nodo_actual = nodo_actual.left

    tree_1.cargo = nodo_actual.cargo

    if hist_nodos != []:
        nodo_padre: BSTree = hist_nodos[-1]
        nodo_padre.left = None


# TEST -----
tree_1 = BSTree(10)
tree_1.left = BSTree(5)
tree_1.right = BSTree(15)

for x in range(20):
    tree_1.insertBST(x)

tree_1.Pre_Order()
borra_raiz(tree_1)
print("-----")
tree_1.Pre_Order()
