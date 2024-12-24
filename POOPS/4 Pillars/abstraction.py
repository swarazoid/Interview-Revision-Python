# Hiding the implementation details of a class and only showing the essential features to a user
# it is implemented using abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # Abstract method: must be implemented by subclasses

    def stop(self):
        print("Default Braking...")  # Abstract method: must be implemented by subclasses

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")


# Example usage
vehicles = [Car(), Bike()]
for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()