from typing import Any


class Tree:
    def __init__(self, cargo: Any, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right

    def nodos(self) -> int:
        resultado: int = 1

        if self.left is None and self.right is None:
            return resultado
        elif self.left is not None:
            resultado += self.left.nodos()
        elif self.right is not None:
            resultado += self.right.nodos()

        return resultado

    def menor_mayor(self) -> tuple:
        menor = mayor = self.cargo
        
        if self.left:
            menor_1 , mayor_1 = self.left.menor_mayor()
            menor = min(menor, menor_1)
            mayor = max(mayor, mayor_1)
        if self.right:
            menor_1 , mayor_1 = self.right.menor_mayor()
            menor = min(menor, menor_1)
            mayor = max(mayor, mayor_1)

        return (menor, mayor)

    def buscar(self, dato: Any) -> bool:
        """
            Retorna True en caso de que dato se encuentre en el árbol
        """
        if self.cargo is None:
            return False
        elif self.cargo == dato:
            return True

        self.left.buscar(dato)
        self.right.buscar(dato)


            
            
    

