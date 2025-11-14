from typing import Any


class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
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

