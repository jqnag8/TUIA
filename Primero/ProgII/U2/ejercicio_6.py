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
            # nodo: _Nodo = nodo.prox

    def filtrar_primos(self) -> listaEnlazada

class ListaDoblementeEnlazada:
    """Modela una lista enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        self.prim: _Nodo = None # Referencia al primer nodo (None si la lista está vacía)
        self.len: int = 0 # Cantidad de elementos de la lista
        self.last: _Nodo = None # Referencia al último Nodo


    def __len__(self) -> None:
        """
            Retorna la cantidad de nodos que hay en la ListaDoblementeEnlazada
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

# ----- Metodos -----    
    def clear(self) -> None:
        """
            Elimina todos los elementos de la ListaDoblementeEnlazada
        """
        self.prim = None


    def count(self, value: Any) -> int:
        """
            Retorna la cantidad de apariciones de 'value' en la ListaDoblementeEnlazada
        """
        resultado: int = 0
        nodo: _Nodo = self.prim

        for _ in range(self.len):
            if nodo.dato == value:
                resultado += 1

            nodo = nodo.prox

        return resultado
    

    def extend(self, lista_1) -> None:
        """
            Enlaza la lista a otra
        """
        self.last = lista_1.last
        self.len += lista_1.len

        return None

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
        elif i == self.len - 1: # insertar en la última posición
            self.last.prox = nuevo
            self.last = nuevo
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
            n_ant = self.prim

            for _ in range(self.len - 2):
                n_ant = n_ant.prox

            dato = self.last.dato
            n_ant.prox = None
            self.last = n_ant
            self.len -= 1
        elif i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
            self.len -= 1
        elif 0 < i < self.len - 1:
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
        else:
            print(" Posición inválida ")
            return

        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista esta vacía")
            return
        elif self.prim.dato == x:
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


    def index(self, valor: Any) -> int | None:
        """
            Retorna el index del elemento en la ListaDoblementeEnlazada
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
            Agrega un elemento al final de la ListaDoblementeEnlazada
        """

        nodo = self.prim
        nodo_nuevo: _Nodo = _Nodo(valor)

        for _ in range(self.len - 1): # Recorremos la ListaDoblementeEnlazada hasta el último nodo
            nodo = nodo.prox

        nodo.prox = self.last = nodo_nuevo
        self.len += 1

        return None


    def rev(self) -> None:
        """
            Revierte el orden de la ListaDoblementeEnlazada
        """
        m: int = 0
        n: int = self.len

        self.prim.dato, self.last.dato = self.last.dato, self.last.dato
        self.prim.prox, self.last.prox = self.last.prox, self.last.prox
        
        while m < n:
            nodo_1: _Nodo = self.prim
            nodo_2: _Nodo = self.prim

            for _ in range(m):
                nodo_1 = nodo_1.prox

            for _ in range(n - 1):
                nodo_2 = nodo_2.prox

            nodo_1.dato, nodo_2.dato = nodo_2.dato, nodo_1.dato
            nodo_1.prox, nodo_2.prox = nodo_2.prox, nodo_1.prox
            m += 1
            n -= 1

        nodo_ult: _Nodo = self.prim

        for _ in range(self.len - 1):
            nodo_ult = nodo_ult.prox

        self.last = nodo_ult

        return None
        
            

# TEST
lst_nodo_1 = ListaDoblementeEnlazada()
lst_nodo_1.insert(0, 10)
print(lst_nodo_1.__len__())
print(lst_nodo_1.__str__())
lst_nodo_1.append(20)
print(lst_nodo_1)

lst_nodo_2 = ListaDoblementeEnlazada()
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
# lst_nodo_1.duplicar(30)
# print(lst_nodo_1)
lst_nodo_1.append(100)
lst_nodo_1.rev()

print(lst_nodo_1)
