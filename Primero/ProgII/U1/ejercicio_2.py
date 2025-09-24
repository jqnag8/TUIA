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

    def __add__(self, other: "Point") -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def distancia(self, other: "Point") -> int | float:
        return pow(1/2, pow(2, self.x - other.x) + pow(2, self.y - other.y))


punto_1 = Point(1,2)
punto_2 = Point(4,6)

print(punto_1.distancia(punto_2))

