# Problematic code

class Vehicle:
    def drive(self):
        print("normal drive")

class SportyVehicle(Vehicle):
    def drive(self):
        print("4 wheel drive")

class FamilyVehicle(Vehicle):
    pass

class OffRoadVehicle(Vehicle):
    def drive(self):
        print("4 wheel drive")


"""
Problem: 
We can see that SportyVehicle and OffRoadVehicle are implementing the drive method, and it has the same algorithm.
So, the drive method code is duplicated, which we don't want ideally.

Crux: 
2 sibling classes are implementing the same method on their own, as they can't get it from parent class

Solution:
Extract out the implementation of the repeating algorithms into set of sepcific algorithms(strategies), and then keep a reference of the startegy according to the context. It's like we are choosing the strategy at runtime, or we set the srategy later.
"""

# Solution code
from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

class NormalDrive(DriveStrategy):
    def drive(self):
        print("normal drive")

class FourWheelDrive(DriveStrategy):
    def drive(self):
        print("4 wheel drive")


class Vehicle():
    def __init__(self):
        self.drive_obj = None

    def set_drive_object(self, drive_obj):
        self.drive_obj = drive_obj

    def drive(self):
        self.drive_obj.drive()

class SportyVehicle(Vehicle):
    pass

class FamilyVehicle(Vehicle):
    pass

class OffRoadVehicle(Vehicle):
    pass


normal_drive = NormalDrive()
four_wheel_drive = FourWheelDrive()

car1 = FamilyVehicle()
car1.set_drive_object(normal_drive)
car1.drive()

car2 = SportyVehicle()
car2.set_drive_object(four_wheel_drive)
car2.drive()