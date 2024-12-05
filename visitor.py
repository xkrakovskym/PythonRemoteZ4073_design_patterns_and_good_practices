from abc import ABC, abstractmethod
from idlelib.window import register_callback
from reprlib import aRepr


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius**2
        print(f"Area of circle: {area}")

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Area of rectangle: {area}")


shapes = [Circle(10), Rectangle(4, 20)]

area_calculator = AreaCalculator()

for shape in shapes:
    shape.accept(area_calculator)
