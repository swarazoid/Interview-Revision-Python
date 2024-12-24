from threading import Thread, Event

class Foo:
    def __init__(self):
        self.first_event = Event()
        self.second_event = Event()

    def first(self, printFirst):
        printFirst()
        self.first_event.set()

    def second(self, printSecond):
        self.first_event.wait()
        printSecond()
        self.second_event.set()

    def third(self, printThird):
        self.second_event.wait()
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
