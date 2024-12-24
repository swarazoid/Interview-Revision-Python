from threading import Thread, Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)
            
    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()
        
    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()
            
    def third(self, printThird):
        self.second_barrier.wait()
        printThird()

# Printing Functions
def printFirst():
    print("First")

def printSecond():
    print("Second")

def printThird():
    print("Third")

# Example Usage
if __name__ == "__main__":
    foo = Foo()

    # Create threads for each method
    t1 = Thread(target=foo.first, args=(printFirst,))
    t2 = Thread(target=foo.second, args=(printSecond,))
    t3 = Thread(target=foo.third, args=(printThird,))

    # Start threads in random order
    t3.start()
    t1.start()
    t2.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()
