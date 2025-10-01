



from typing import Any

class _Nodo:
    def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def ver_lista(nodo) -> None:
        """Recorre todos los nodos a través de sus enlaces, mostrando sus
        contenidos.
        """
        while nodo is not None:
            print(nodo)
            nodo = nodo.prox

class ListaEnlazada:
    """Modela una lista enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or self.len < i:
            print("Posición inválida")
            return

        nuevo = _Nodo(x)

        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for _ in range(1, i):
                n_ant = n_ant.prox

            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        self.len += 1

    def pop(self, i: int | None = None) -> Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """
        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            print(" Posición inválida ")
            return

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
            self.len -= 1
        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista esta vacía")
            return
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
            self.len -= 1

    def __len__(self) -> None:
        """
            Retorna la cantidad de nodos que hay en la ListaEnlazada
        """
        return self.len
       
    def __str__(self):
        """Completar"""

        nodo = self.prim
        resultado: str = "["

        while nodo is not None:
            resultado += f"{nodo.dato}, "
            nodo = nodo.prox

        resultado = resultado[:-2]
        resultado += "]"
        return resultado

    def index(self, valor: Any) -> int | None:
        """
            Retorna el index del elemento en la ListaEnlazada
        """
        
        nodo: _Nodo = self.prim
        contador: int = 0

        while nodo is not None:
            if nodo.valor == valor:
                return contador
            nodo = nodo.prox
            contador += 1

        print("No se encuentra en la lista")
        return None

    def append(self, valor: Any) -> None:
        """
            Agrega un elemento al final de la ListaEnlazada
        """

        nodo = self.prim
        nodo_nuevo = _Nodo(valor)

        for _ in range(self.len - 1): # Recorremos la ListaEnlazada hasta el último nodo
            nodo = nodo.prox

        nodo.prox = nodo_nuevo
        self.len += 1

        return None

    def extend(self, lista_1) -> None:
        """
            Enlaza la lista a otra
        """
        nodo = self.prim

        for _ in range(self.len - 1): # Recorremos la ListaEnlazada hasta el último nodo
            nodo = nodo.prox

        nodo.prox = lista_1.prim # Enlaza el último elemento de la primera lista con el primero de la segunda
        self.len += lista_1.len

        return None

    def remover_todos(self, dato: Any) -> int:
        """
            Remueve todas las apariciones del 'dato' en la ListaEnlazada
        """
        nodo: _Nodo = self.prim
        contador: int = 0
        pos_apariciones: list[int] = list() # Guarda las posiciones en las que aparece 'dato'

        while nodo is not None:
            if nodo.dato == dato:
                pos_apariciones += [contador]
            nodo = nodo.prox
            contador += 1

        for pos in pos_apariciones[::-1]:
            self.pop(pos)

        return len(pos_apariciones)

    def duplicar(self, elemento: Any) -> None:
        """
            Duplica todas las apariciones del 'elemento' en la ListaEnlazada
        """
        contador: int = 0
        lista_apariciones: list[int] = list()
        nodo: _Nodo = self.prim

        while nodo is not None:
            if nodo.dato == elemento:
                lista_apariciones += [contador]
            nodo = nodo.prox
            contador += 1

        for pos in lista_apariciones:
            self.insert(pos + 1, elemento)

        return None

    def rev(self) -> None:
        """
            Revierte el orden de la ListaEnlazada
        """
        
            
            

# TEST
lst_nodo_1 = ListaEnlazada()
lst_nodo_1.insert(0, 10)
print(lst_nodo_1.__len__())
print(lst_nodo_1.__str__())
lst_nodo_1.append(20)
print(lst_nodo_1)

lst_nodo_2 = ListaEnlazada()
lst_nodo_2.insert(0, 50)
print(lst_nodo_2.__len__())
print(lst_nodo_2.__str__())
lst_nodo_1.extend(lst_nodo_2)
lst_nodo_1.insert(1, 100)
lst_nodo_1.append(100)
lst_nodo_1.append(100)
lst_nodo_1.append(100)
print(lst_nodo_1)
lst_nodo_1.remover_todos(100)
print(lst_nodo_1)
lst_nodo_1.duplicar(30)
print(lst_nodo_1)
