"""
Use case: What it solves is, once we have completed a class, and it is fully tested, we don't want to add any method to that class(no edit). Eg: Libraries
So, it separates out the operations from the object on which it operates

Double dispatch: So generally, when we do obj.something(), the something function is decided by the obj itself. This is called single dispatch, where the actual function to be called is decided by 1 object.
When function is decided by 2 objects, 1 caller and 1 argument, it is called DOuble dispatch.
For example: room1.accept(price_calculator) code in the below code, the actual method to be called is decided by room1 and price_calculator objects.

Honestly this design pattern looks just over complicating things, maybe an understanding gap as of now.
"""

# sample use case: Hotel rooms

from abc import ABC, abstractmethod

# Base class for Visitors
class Visitor(ABC):
    @abstractmethod
    def visit_single_room(self, room):
        pass

    @abstractmethod
    def visit_suite_room(self, room):
        pass


# Concrete Visitors
class PriceCalculator(Visitor):
    def visit_single_room(self, room):
        print(f"Calculating price for Single Room: Base Price: {room.base_price}")
        return room.base_price * 1.1  # Example: Adding 10% tax

    def visit_suite_room(self, room):
        print(f"Calculating price for Suite Room: Base Price: {room.base_price}")
        return room.base_price * 1.2  # Example: Adding 20% tax


class RoomCleaner(Visitor):
    def visit_single_room(self, room):
        print(f"Cleaning Single Room: {room.room_number}")

    def visit_suite_room(self, room):
        print(f"Cleaning Suite Room: {room.room_number}")


# Base class for Hotel Rooms
class Room(ABC):
    def __init__(self, room_number, base_price):
        self.room_number = room_number
        self.base_price = base_price

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# Concrete Room Types
class SingleRoom(Room):
    def accept(self, visitor: Visitor):
        # Double dispatch: Pass self to the visitor's appropriate method
        return visitor.visit_single_room(self)


class SuiteRoom(Room):
    def accept(self, visitor: Visitor):
        # Double dispatch: Pass self to the visitor's appropriate method
        return visitor.visit_suite_room(self)


# Example usage
if __name__ == "__main__":
    # Rooms
    room1 = SingleRoom(room_number=101, base_price=100)
    room2 = SuiteRoom(room_number=201, base_price=300)

    # Visitors
    price_calculator = PriceCalculator()
    room_cleaner = RoomCleaner()

    # Calculate prices
    print(f"Price for room 101: {room1.accept(price_calculator)}")
    print(f"Price for room 201: {room2.accept(price_calculator)}")

    # Clean rooms
    room1.accept(room_cleaner)
    room2.accept(room_cleaner)


"""
This looks similar to strategy pattern, where we pass in the strategy to be used.
The difference is in strategy pattern we outsource the algorithm, and any combination can be used as per need, but in this pattern methods are tied to the class actually, just that they are written outside, but we won't call price_calculator of suite room  for single room price calculation.
"""