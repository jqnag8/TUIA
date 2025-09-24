class Automovil:
    def __init__(self, pat: str, marca: str, km_rec: float = 0, lt_nafta: float = 0):
        self.pat = pat
        self.marca = marca
        self.km_rec = km_rec
        self.lt_nafta = lt_nafta

    def avanzar(self, km_cond) -> None:
        resultado = (km_cond * 8.8) / 100

        if self.lt_nafta - resultado < 0:
            print("Es necesario cargar nafta para recorrer la cantidad de km")
        else:
            self.km_rec += km_cond
            self.lt_nafta -= resultado
            

    def cargar_nafta(self, cant_nafta: int) -> None:
        """
            Suma la cantidad de nafta cargada
        """

        self.lt_nafta += cant_nafta


test = Automovil("111", "Chevrolet", 1, 1000)

test.avanzar(100000000000)

print(test.km_rec, test.lt_nafta)
