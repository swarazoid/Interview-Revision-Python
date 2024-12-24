"""
Use case: might not be a really useful design Pattern. It is used such that instead of returning null from some code paths, we always return some object with the expected interface, so that we don't get null pointer exception.
"""

# sample use case used with factory

from abc import ABC, abstractmethod

class ShapeInterface(ABC):
    @abstractmethod
    def draw():
        pass

class Circle(ShapeInterface):
    def draw(self):
        print("Draw a circle")

class Triangle(ShapeInterface):
    def draw(self):
        print("Draw a Triangle")

class DefaultShape(ShapeInterface):
    def draw(self):
        print("Unknown shape")

class ShapeFactory():
    def get_shape_based_on_sides(self, no_of_sides):
        if no_of_sides == 0:
            return Circle()
        elif no_of_sides == 3:
            return Triangle()
        else:
            # don't return null here
            return DefaultShape()

if __name__ == "__main__":
    shape_factory = ShapeFactory()
    triangle = shape_factory.get_shape_based_on_sides(3)
    triangle.draw()
    circle = shape_factory.get_shape_based_on_sides(0)
    circle.draw()
    random_shape = shape_factory.get_shape_based_on_sides(7)
    random_shape.draw()