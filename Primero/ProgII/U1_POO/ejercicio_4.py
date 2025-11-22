class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def mueve(self, orden: str) -> None:
        match orden:
            case 'A' | 'a':
                self.y += 1
            case 'R' | 'r':
                self.y -= 1
            case 'I' | 'i':
                self.x -= 1
            case 'D' | 'd':
                self.x += 1

    def posicion_actual(self):
        return f"El robot se encuentra en las coordenadas ({self.x}, {self.y})"


mi_robot = Robot()
orden = input("Introduce la orden: ")
while orden != 'fin':
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden: ")
