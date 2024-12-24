class Student():
    salary = 0 # class attribute
    college = None

    def __init__(self, name): # gets executed whenever an object is instantiated
        self.name = name # instance attribute

    @staticmethod # does not need self to be passed, independent of class or instance
    def welcome():
        print("welcome student")

    @classmethod # can access class level attributes
    def change_college(cls, clg_name):
        cls.college = clg_name
        print(cls.college)

    def get_name(self):
        print(self.name)

s1 = Student("Rahul")
s2 = Student("Ronaldo")

s1.new_instance_var = 7
s1.salary = 5 # this creates new var salary for s1 object, not changes for Student class
Student.salary = 10 

Student.welcome()
s1.welcome() # this line won't work if the staticmethod decorator is not used

Student.change_college("lol")
s1.change_college("bol") # this line also changes the class attribute
print(Student.college)