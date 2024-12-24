from threading import Thread, Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()


# Printing Functions
def printFirst():
    print("first", end=" ")

def printSecond():
    print("second", end=" ")

def printThird():
    print("third", end=" ")

# Example Usage
if __name__ == "__main__":
    foo = Foo()

    t1 = Thread(target=foo.first, args=(printFirst,))
    t2 = Thread(target=foo.second, args=(printSecond,))
    t3 = Thread(target=foo.third, args=(printThird,))

    # Start threads in a random order
    t3.start()
    t2.start()
    t1.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
