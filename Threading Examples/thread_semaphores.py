from threading import Thread, Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))
        
    def first(self, printFirst):
        printFirst()
        self.gates[0].release()
        
    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()
            
    def third(self, printThird):
        with self.gates[1]:
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
