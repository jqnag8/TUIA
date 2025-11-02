class Stack:
    def __init__(self):
        self.items = []

    def push(self, x: int):
        while type(x) is not int:
            x = int(input("Ingrese un tipo de dato int: "))

        self.items.append(x)

    def pop(self) -> int | None:
        if self.is_empty():
            print("Está vacía")
            return 
        else:
            return self.items.pop()

    def is_empty(self) -> bool:
        return self.items == []

    def mostrar_Pila(self) -> None:
        for elem in self.items:
            print(elem)

def reordenar_stack(stack_1: Stack) -> None:
    """
        Reordena los elementos del stack de forma que los numeros pares aperecen primeros
    """
    if stack_1.is_empty():
        print("El Stack se encuentra vacío")
        return
        
    stack_par = Stack()
    stack_imp = Stack()
    long = len(stack_1.items)

    for _ in range(long):
        num = stack_1.pop()

        if num % 2 == 0:
            stack_par.push(num)
        else:
            stack_imp.push(num)

    long = len(stack_par.items)

    for _ in range(long):
        num = stack_par.pop()

        stack_1.push(num)

    long = len(stack_imp.items)

    for _ in range(long):
        num = stack_imp.pop()

        stack_1.push(num)
        return 
