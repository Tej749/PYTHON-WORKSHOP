from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sount(self):
        pass

class Dog(Animal):
    def make_sount(self):
        return 'roar'

class Cat(Animal):
    def make_sount(self):
        return "meow"


x = [Dog(), Cat()]
for animal in x:
    print(animal)

