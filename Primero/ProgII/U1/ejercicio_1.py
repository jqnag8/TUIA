# ----- 1 ------
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    
class Rectangle:
    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return f"Rectángulo ubicado en ({self.width}, {self.height}) con ángulo de {self.corner}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.width == other.width and self.height == other.height and self.corner.__eq__(other.corner)


punto_1 = Point(1, 2)
punto_2 = Point(-5, 7)
rectangulo_1 = Rectangle(3, 4, punto_1)
rectangulo_2 = Rectangle(6, 9, punto_2)


print(rectangulo_1.__str__())
print(rectangulo_2.__str__())
print(rectangulo_1.__eq__(rectangulo_1))


# ----- 2 -----

def mover_rectangulo_pura(rectangulo_1: Rectangle, dx: int, dy: int) -> Rectangle:
    """cambia de posición el rectángulo sumando dx a la coordenada x de la
    esquina superior izquierda y del mismo modo sumar dy a la coordenada y de la esquina superior
    izquierda."""

    resultado = Rectangle(rectangulo_1.width, rectangulo_1.height, rectangulo_1.corner)
    resultado.corner.x += dx
    resultado.corner.y += dy

    return resultado
    

def mover_rectangulo_modificadora(rectangulo_1: Rectangle, dx: int, dy: int) -> None:
    rectangulo_1.corner.x += dx
    rectangulo_1.corner.y += dy



mover_rectangulo_modificadora(rectangulo_1, 5, 10)
print(rectangulo_1.__str__())
print(mover_rectangulo_pura(rectangulo_2, 5, 10))
