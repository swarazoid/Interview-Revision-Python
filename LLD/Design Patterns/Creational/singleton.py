"""
Use case: We want only 1 instance of a class globally, for eg: db connection when once done, we can keep reusing it.
There are 4 ways to instantiate the class:
1. Eager
2. Lazy
3. Synchronized
4. Double Locking - used most widely in industry
"""

# Eager code:
class SingletonEager:
    # Instance is created when the class is loaded (eager initialization)
    _instance = super().__new__(object)
    
    def __new__(cls):
        return cls._instance

# Usage
singleton1 = SingletonEager()
singleton2 = SingletonEager()
print(singleton1 is singleton2)  # Output: True


# Lazy code:
class SingletonLazy:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLazy, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = SingletonLazy()
singleton2 = SingletonLazy()
print(singleton1 is singleton2)  # Output: True


# Synchronized code: The problem is every caller will acquire lock once and then release
import threading

class SingletonSynchronized:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonSynchronized, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = SingletonSynchronized()
singleton2 = SingletonSynchronized()
print(singleton1 is singleton2)  # Output: True


# Double Locking code: In this only the first time, multiple instanciators can acquire the lock, not after that.
import threading

class SingletonDoubleChecked:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Locking only when instance is None
                if cls._instance is None:  # Double check
                    cls._instance = super(SingletonDoubleChecked, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = SingletonDoubleChecked()
singleton2 = SingletonDoubleChecked()
print(singleton1 is singleton2)  # Output: True


"""
Notes:
Calling Order of __new__ and __init__
__new__: This method is called first. It is responsible for creating a new instance of the class. If a class doesn't implement __new__, Python uses the __new__ method from its parent class (object).

__init__: After the instance is created by __new__, Python automatically calls the __init__ method to initialize the instance. The __init__ method does not create the instance but instead initializes the newly created object by setting attributes or performing other setup tasks.

Do __new__ and __init__ get called every time?
The behavior of __new__ and __init__ depends on the Singleton implementation. Here's the general rule:

__new__ is always called every time you create a new object, but it can be used to control whether the same instance is returned or a new instance is created.
__init__ is only called once for a particular object during its initialization (unless the object is explicitly reinitialized or a new instance is created). In a Singleton pattern, we ensure that __init__ is called only once per instance.
"""

# Code with args:
class SingletonLazy:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance if it does not exist
            cls._instance = super(SingletonLazy, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, '_initialized'):  # Ensure initialization happens only once
            self.name = name
            self._initialized = True

s = SingletonLazy("my name")


"""
What does super(SingletonLazy, cls).__new__(cls) actually mean?

super(SingletonLazy, cls):
- super() is a built-in function in Python used to call methods from a parent or superclass.
- super(SingletonLazy, cls) is used to get the parent class of SingletonLazy (which is object, the base class of all Python classes).
- The super() call returns a proxy object that delegates method calls to the next class in the method resolution order (MRO). In this case, super(SingletonLazy, cls) returns a proxy to object, since SingletonLazy is ultimately inheriting from object.

__new__(cls):
- __new__(cls) is the method that actually creates the instance of a class. It is responsible for returning a new object instance, whereas __init__(self) is responsible for initializing the instance (i.e., setting its attributes).
- Here, cls is the class itself, which in the case of __new__ is SingletonLazy.

So, super(SingletonLazy, cls).__new__(cls) is equivalent to calling object.__new__(cls) — it tells Python to create a new instance of the SingletonLazy class using the __new__ method from the parent class (object), which is the default behavior for creating objects.

Why use super() instead of object.__new__(cls) directly?
Using super() is preferred for two main reasons:

- It allows the class to be more flexible and easier to subclass. If you use object.__new__(cls) directly, it would tightly couple the code to the base object class, making it harder to change the inheritance structure.
- In Python, the super() function works well in multiple inheritance scenarios. It ensures the method is called in the correct order according to the Method Resolution Order (MRO), allowing for better compatibility if the class is involved in multiple inheritance.
"""

