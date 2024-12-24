"""
Use Case: when ever we have a constructor which might have lots of optional field(say 10). We might not want to pass 10 items from everywhere we try to create the object.
How is it solved:
Take a builder class very similar to original class and setter methods for all the attributes. Update that builder class by calling all the required setter methods. Call build() method at the end to finally instanciate the original class with all the attributes taken from the builder object.
"""

# sample use case: create a student builder that builds student step by step

class Student:
    def __init__(self, builder):
        self.name = builder.name
        self.age = builder.age
        self.grade = builder.grade
        self.school = builder.school
        self.major = builder.major
        self.gpa = builder.gpa

    def __str__(self):
        return (f"Student(Name: {self.name}, Age: {self.age}, Grade: {self.grade}, "
                f"School: {self.school}, Major: {self.major}, GPA: {self.gpa})")

class StudentBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.grade = None
        self.school = None
        self.major = None
        self.gpa = None

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_grade(self, grade):
        self.grade = grade
        return self

    def set_school(self, school):
        self.school = school
        return self

    def set_major(self, major):
        self.major = major
        return self

    def set_gpa(self, gpa):
        self.gpa = gpa
        return self

    def build(self):
        return Student(self)

# Example usage:
if __name__ == "__main__":
    student_builder = StudentBuilder()
    student = (student_builder
               .set_name("Alice")
               .set_age(20)
               .set_grade("Sophomore")
               .set_school("XYZ University")
               .set_major("Computer Science")
               .set_gpa(3.8)
               .build())
    print(student)

"""
Questions: 
Why do we need a builder class, why can't we just have all the setter methods in the Student class itself, and instanciate the student calss empty and then update all the attributes?
- Generally it is not a good idea to instanciate an empty class and then fill it. Another reason is we might want to create immutable Student class, which will become difficult if we give setters in student class.

For the pizza maker example, can we use builder pattern instead of decorator patter?
- We should not. We can create a Pizza builder class that will have setters for toppings, but we will have to update this builder class, which will violate the open close principle.

Key Difference
The key difference lies in when and how the decisions are made:
- Builder(creational design pattern): Decisions are made before the object is created. Once the object is built, it's immutable. You can decide dynamically during the building process, but the object itself remains fixed after construction.
- Decorator(structural design pattern): Decisions can be made after the object is created. You can dynamically modify or extend the object at runtime, without needing to rebuild or recreate it.
"""