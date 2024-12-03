from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal je abstraktní bázová třída (ABC). Definuje smlouvu pro
    podtřídy, která zajišťuje, že implementují metodu `make_sound`.
    Animal má pouze abstraktní metody a teda funguje jako rozhraní.
    """
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return "Animal is eating"


class FourLeggedAnimal(ABC):
    @abstractmethod
    def run(self):
        pass


class Dog(Animal, FourLeggedAnimal):
    def make_sound(self):
        return "Woof!"

    def run(self):
        return "Dog is running..."

class Cat(Animal):
    def make_sound(self):
        return "Meow!"