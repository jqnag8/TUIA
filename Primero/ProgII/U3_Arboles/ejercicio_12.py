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

    def borra_raiz(self: 'BSTree') -> None:
        """Elimina la raiz del arbol y la reemplaza por otra usando el metodo in order"""

        if self.right is None:
            nodo_actual: BSTree = self.left
            self.cargo = nodo_actual.cargo
            self.left = nodo_actual.left
            self.right = nodo_actual.right
            return 

        nodo_actual = self.right
        hist_nodos: list[BSTree] = list()

        while nodo_actual.left is not None:
            hist_nodos += [nodo_actual]
            nodo_actual = nodo_actual.left

        self.cargo = nodo_actual.cargo

        if hist_nodos != []:
            nodo_padre: BSTree = hist_nodos[-1]
            nodo_padre.left = None


# Funciones -----

def borrar_valor(tree_1: BSTree, elemento: Any) -> None:
    """Elimina el elemento del arbol"""
    nodo_actual: BSTree = tree_1

    while nodo_actual is not None and nodo_actual.cargo != elemento:
        if nodo_actual.cargo > elemento:
            nodo_actual = nodo_actual.left
        if nodo_actual.cargo < elemento:
            nodo_actual = nodo_actual.right

    if nodo_actual is not None:
        nodo_actual.borra_raiz()
        return None
    else:
        print("El elemento no se encuentra en la raíz")
        return None


# TEST
