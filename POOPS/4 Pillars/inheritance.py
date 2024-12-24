# when 1 class(child/derived) derives its properties and methods from another class(parent/base)

class A():
    def __init__(self, name):
        self.name = name
        print("init from A, name = ", name)

    @staticmethod
    def show():
        print("from class A")

class B():

    def __init__(self, age):
        print("init from B, age = ", age)

    @staticmethod
    def show():
        print("from class B")
    
    def show_again(self):
        print("show again from B")

class C(A, B): # resolution mostly follows DFS

    def __init__(self, name, age):
        super().__init__(name)
        A.__init__(self, name)
        B.__init__(self, age)
        self.age = age

    @staticmethod
    def show_from_c():
        print("show from C")


s = C("name", 30)
s.show()
s.show_again()
s.show_from_c()

print(C.__mro__) # prints method resolution order