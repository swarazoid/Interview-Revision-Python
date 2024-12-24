from threading import Thread, Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        
    def first(self, printFirst):
        printFirst()
        self.locks[0].release()
        
    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()
            
    def third(self, printThird):
        with self.locks[1]:
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
