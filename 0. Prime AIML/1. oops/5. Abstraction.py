# ABC module is used to create abstract classes in python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # decorator is used to convert a method into an abstract method
    def make_sound(self):
        pass # This is a placeholder for the abstract method


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()