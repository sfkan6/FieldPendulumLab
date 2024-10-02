
class Point:
    def __init__(self, x: int|float, y: int|float) -> None:
        self.setPoint(x, y)

    def setPoint(self, x: int|float, y: int| float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

