# Write your solution here!


class Pair:
    _first: int
    _second: int

    def __init__(self, first: int, second: int) -> None:
        self._first = first
        self._second = second

    def __getitem__(self, index: int) -> int:
        return self._first if index == 0 else self._second

    def __setitem__(self, index: int, value: int) -> None:
        print("Error: Pair is immutable!")
        return

    def __eq__(self, other) -> bool:
        return self._first == other[0] and self._second == other[1]

    def __repr__(self) -> str:
        return f"({self._first}, {self._second})"
