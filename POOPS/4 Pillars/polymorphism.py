# Polymorphism is a concept that allows methods in different classes to have the same name but behave differently based on the class they belong to

# Python supports polymorphism through:
# Duck Typing: Behavior determined by the object's methods/attributes rather than its type.
# Method Overriding: Subclasses provide specific implementations of methods defined in the parent class.

# Example 1: Polymorphism Through Duck Typing
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

# Polymorphic function
def make_sound(animal):
    print(animal.sound())

# Usage
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    make_sound(animal)


# Example 2: Polymorphism Through Method Overriding
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Polymorphic behavior
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
