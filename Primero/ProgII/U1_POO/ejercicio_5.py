class Robot:
    def __init__(self):
        self.historial: str = ''
        self.x = 0
        self.y = 0

    def mueve(self, sec_orden: str) -> None:
        """
        Recibe una secuencia de ordenes y modifica la posición del robot y guarda
        la orden en el historial.
        """
        for orden in sec_orden:
            match orden:
                case 'A' | 'a':
                    self.y += 1
                    self.historial += orden
                case 'R' | 'r':
                    self.y -= 1
                    self.historial += orden
                case 'I' | 'i':
                    self.x -= 1
                    self.historial += orden
                case 'D' | 'd':
                    self.x += 1
                    self.historial += orden
                case _:
                    print("Orden no válida")

    def posicion_actual(self):
        """
        Retorna la posicion actual del robot
        """
        return f"El robot se encuentra en las coordenadas ({self.x}, {self.y})"

    def obtener_historico_de_movimientos(self):
        """
        Retorna el historial de movimientos del Robot
        """
        return self.historial

    def como_volver(self):
        """
        Retorna un string indicando los movimientos que el robot debería de
        realizar para llegar a la posición (0,0)
        """
        index = len(self.historial) - 1
        resultado: str = ""

        while index <= 0:
            resultado += self.historial[index]  # Añadimos la última orden a resultado
            index -= 1

        return resultado


mi_robot = Robot()
orden = input("Introduce la orden: ")
while orden != "fin":
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden: ")
