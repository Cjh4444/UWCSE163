class MySet:
    """
    MySet should have the following behaviors:

    The MySet class should only store non-negative int values in its hash table.

    You may assume the input values don’t collide in the hash table.
    This means you
    do not need to implement separate chaining. Recall that a collision is when two
    different values end up at the same index.

    Your hash table should be fixed-size and you shouldn’t ever rehash. Make your
    hash table be size 10 and store it as a field with type list.

    You should implement these functions so that they all have complexity O(1).
    For this checkpoint, this means your program should not have any loops!

    All fields should be private.

    You should not use the set class in any way in your implementation. You
    should implement MySet using a list as your hash table.
    """

    def __init__(self) -> None:
        self._table = [0] * 10
        self._size = 0

    def add(self, value: int) -> None:
        hash_val = value % 10

        if (value not in self) and (self._table[hash_val] == 0):
            self._table[hash_val] = value
            self._size += 1

    def __contains__(self, value: int) -> bool:
        return self._table[value % 10] == value

    def __len__(self) -> int:
        return self._size

    pass