# Write your Point class here
class Point:
    _x: int
    _y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x) -> None:
        self.x = x

    def set_y(self, y) -> None:
        self.y = y

    def display(self) -> str:
        return f"({self.x}, {self.y})"
