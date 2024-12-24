"""
Use case: Assume we have a class where the constructor is very expensive to run, example it might make many network requests. And now we wan tto have many similar objects, with just minor changes. We might not want to create all objects from scratch everytime as I said, the constructor is very expensive to run. So what we do? We clone the existing object.

But if we simply try to copy, we can get into problems like:
- not able to access private attributes and methods.
- not able to copy object refrences within the object(eg: list), we would like fresh copies

So what we do is the original class itself exposes a clone method which everyone can call and get the clone

Python gives us deepcopy. It copies literally everything. private variables with dunder too.
"""

# sample use case: create a student class and try to copy the student

from abc import ABC, abstractmethod
import copy

# Define the Prototype interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Define the Student class that implements the Prototype interface
class Student(Prototype):
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        self.__moreprivate = "This is a more private variable"  # Name mangling example

    def clone(self):
        # The clone method creates a deep copy of the current object
        return copy.deepcopy(self)

    def get_private(self):
        return self.__moreprivate

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Grades: {self.grades}, Private Var: {self.__moreprivate})"

# Create an instance of Student
student1 = Student("Alice", 21, [85, 90, 88])

# Clone the student using the prototype pattern
student2 = student1.clone()

# Modify the original object
student1.name = "Bob"
student1.grades[0] = 95
student1._Student__moreprivate = "Modified more private variable"  # Accessing mangled name directly

# Output the original and cloned students
print("Original student:", student1)
print("Cloned student 1:", student2)
