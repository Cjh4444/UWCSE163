# Write your solution here!
from dog import Dog


class DogPack:
    _dogs: list[Dog]

    def __init__(self) -> None:
        self._dogs = []

    def add_dog(self, dog: Dog) -> None:
        self._dogs.append(dog)

    def all_bark(self) -> None:
        for dog in self._dogs:
            dog.bark()
