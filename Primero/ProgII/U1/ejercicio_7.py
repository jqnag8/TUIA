class Cosa:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"{self.valor}"

class Coleccion:
    def __init__(self, coleccion1 = []):
        self.coleccion = coleccion1

    def agregar_cosa(self, cosa: Cosa):
        self.coleccion.append(cosa)
        
    def __str__(self):

        resultado = [str(x.valor) for x in self.coleccion]

        return f"{resultado}"


cosa = Cosa(10)
coleccion = Coleccion()
coleccion.agregar_cosa(cosa)
print(coleccion)
