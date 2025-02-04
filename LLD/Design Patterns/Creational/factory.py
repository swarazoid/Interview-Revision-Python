"""
Use case: 
Whenever we find to many if else at too many places to decide which obj needs to be create, we create a separate class and write the if else logic in that to create the object and return
"""

# Sample use case: get shape class based on some condition like number of sides

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

class ShapeFactory():
    @staticmethod
    def get_shape_based_on_sides(no_of_sides):
        if no_of_sides == 0:
            return Circle()
        elif no_of_sides == 3:
            return Triangle()

if __name__ == "__main__":
    triangle = ShapeFactory.get_shape_based_on_sides(3)
    triangle.draw()
    circle = ShapeFactory.get_shape_based_on_sides(0)
    circle.draw()