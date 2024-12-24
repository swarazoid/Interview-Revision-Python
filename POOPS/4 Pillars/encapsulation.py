# Wrapping data and functions into a single unit (object)
# Literally means creating classes

# Key Aspects of Encapsulation in Python
# Data Hiding:
#       Python achieves this using access specifiers:
#       Public: Accessible from anywhere.
#       Protected: Indicated by a single underscore (_), suggesting that it’s meant for internal use but not enforced.
#       Private: Indicated by double underscores (__), which triggers name mangling to make the attribute harder to access directly.
# Controlled Access:
#       You can provide getter and setter methods to control how data is accessed and modified.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if name.strip():
            self.__name = name
        else:
            raise ValueError("Name cannot be empty!")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive!")

# Usage
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.set_age(35)        # Correctly modifying age
print(person.get_age())   # Output: 35

# person.set_age(-5)      # Raises ValueError: Age must be positive!


# using @property decorator
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Property for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            raise ValueError("Name cannot be empty!")

    # Property for age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be positive!")

# Usage
person = Person("Alice", 30)
print(person.name)   # Output: Alice
person.age = 35      # Correctly setting age
print(person.age)    # Output: 35

# person.age = -5    # Raises ValueError: Age must be positive!


# If you define a @property, a corresponding setter is not mandatory. Without a setter, the property becomes read-only.
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius  # Read-only attribute

circle = Circle(5)
print(circle.radius)  # Output: 5

# circle.radius = 10  # Raises AttributeError: can't set attribute


# Encapsulation vs. Abstraction
# Encapsulation focuses on restricting access to data and methods to protect them.
# Abstraction focuses on hiding implementation details to simplify interaction with an object. Encapsulation can be seen as a tool to implement abstraction.