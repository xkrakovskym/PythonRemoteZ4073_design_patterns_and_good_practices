"""
class Bird:
    def fly(self):
        return "I am flying!"


class Sparrow(Bird):
    def fly(self):
        return "I am a sparrow, and I am flying!"


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches cannot fly!")
"""

from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        return "I am flying!"


class NonFlyingBird(Bird):
    def move(self):
        return "I am walking!"


class Sparrow(FlyingBird):
    pass


class Ostrich(NonFlyingBird):
    pass
