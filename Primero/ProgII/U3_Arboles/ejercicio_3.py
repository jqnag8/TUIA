from typing import Any


class Pila:
    def __init__(self):
        self.items = []

    def push(self, x: Any):
        self.items.append(x)

    def pop(self) -> Any | None:
        if self.is_empty():
            print("Está vacía")
            return None
        else:
            return self.items.pop()

    def is_empty(self) -> bool:
        return self.items == []

    def mostrar_Pila(self) -> None:
        for elem in self.items:
            print(elem)

class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

    # -- Recursivas --
    def Pre_Order(self) -> None:
        """Realiza un recorrido Pre Order por el árbol"""
        sl = self.left
        sr = self.right

        print(self.cargo)

        if sl is not None:
            sl.Pre_Order()

        if sr is not None:
            sr.Pre_Order()

    def In_Order(self) -> None:
        """Realiza un recorrido In Order por el árbol"""
        sl = self.left
        sr = self.right

        if sl is not None:
            sl.In_Order()

        print(self.cargo)

        if sr is not None:
            sr.In_Order()

    def Post_Order(self) -> None:
        """Realiza un recorrido Post Order por el árbol"""
        sl = self.left
        sr = self.right

        if sl is not None:
            sl.Post_Order()

        if sr is not None:
            sr.Post_Order()

        print(self.cargo)

    # -- Iterativas --
    def pre_order_iter(self) -> None:
        """Realiza un recorrido Pre Order por el árbol"""
        p = Pila()

        p.push(self)

        while not p.is_empty():
            nodo_actual = p.pop()
            print(nodo_actual.cargo)

            if nodo_actual.right is not None:
                p.push(nodo_actual.right)

            if nodo_actual.left is not None:
                p.push(nodo_actual.left)


    def in_order_iter(self) -> None:
        """Realiza un recorrido In Order por el árbol"""
        p = Pila()
        nodo_actual = self
        p.push(nodo_actual)

        while not p.is_empty():
            while nodo_actual is not None and nodo_actual.left is not None:
                nodo_actual = nodo_actual.left
                p.push(nodo_actual)
           
            nodo_visitar = p.pop()
            print(nodo_visitar.cargo)
            nodo_actual = nodo_visitar.right

            if nodo_actual is not None:
                p.push(nodo_actual)
            

    def post_order_iter(self) -> None:
        """Realiza un recorrido Post Order por el árbol"""
        p_resultado = Pila()
        p_trabajo = Pila()
        p_trabajo.push(self)

        while not p_trabajo.is_empty():
            nodo_actual = p_trabajo.pop()
            p_resultado.push(nodo_actual)
            
            if nodo_actual.left is not None:
                p_trabajo.push(nodo_actual.left)

            if nodo_actual.right is not None:
                p_trabajo.push(nodo_actual.right)
           
        while not p_resultado.is_empty:
            nodo_imprimir = p_resultado.pop()
            print(nodo_imprimir.cargo)


# TEST
tree_1 = Tree(10)
tree_2 = Tree(20)
tree_3 = Tree(30, tree_2, tree_1)
tree_4 = Tree(40, None, tree_3)
tree_5 = Tree(50)
tree_6 = Tree(60, tree_5, None)
tree_7 = Tree(70, tree_6, tree_4)

print("Pre_Order: ")
tree_7.Pre_Order()
print("In_Order: ")
tree_7.In_Order()
print("Post_Order: ")
tree_7.Post_Order()

print("Iterativos")
print("Pre_Order: ")
tree_7.pre_order_iter()
print("In_Order: ")
tree_7.in_order_iter()
print("Post_Order: ")
tree_7.post_order_iter()
