# Write your Point class here
class Point:
    _x: int
    _y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def display(self) -> str:
        return f"({self.x}, {self.y})"
