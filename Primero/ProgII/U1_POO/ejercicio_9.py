class Entidad:
    def __init__(self, vida_inicial: int):
        self.vida = vida_inicial
        


class Enemigo(Entidad):
    pass


class Jugador(Entidad):
    def __init__(self, vida_inicial: int):
        super().__init__(vida_inicial)
        self.enemigos_golpeados = []

    def golpeado(self, cuanto: int):
        """
            Quita 'cuanto' vida al Jugador
        """
        self.vida -= cuanto

    def golpear(self, enemigo: Enemigo, cuanto: int):
        """
            Quita 'cuanto' vida al enemigo y lo agrega a la lista de los enemigos golpeados
        """
        enemigo.vida -= cuanto
        self.enemigos_golpeados += [enemigo]
