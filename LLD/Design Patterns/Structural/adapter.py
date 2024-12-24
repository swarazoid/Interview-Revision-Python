"""
Use case: this design pattern is just a adapter between clients and the final object.
If clients use the final object directly, if something changes in the final object, all clients have to update their code.
So we create an adapter in between, which only needs to update its logic when the final object changes.
"""

# sample use case: weight machine converter from pounds to kg

from abc import ABC, abstractmethod

# Target Interface
class IWeightMachine(ABC):
    """Interface for the weight machine."""
    @abstractmethod
    def get_weight_in_pounds(self):
        """Returns the weight in pounds."""
        pass


# Adaptee Implementation
class WeightMachine(IWeightMachine):
    """Concrete implementation of the weight machine."""
    def get_weight_in_pounds(self):
        """Return the weight in pounds."""
        return 150  # Example weight in pounds


# Adapter Interface
class IWeightMachineAdapter(ABC):
    """Interface for the weight machine adapter."""
    @abstractmethod
    def get_weight_in_kilograms(self):
        """Convert weight to kilograms."""
        pass

    @abstractmethod
    def get_weight_in_stones(self):
        """Convert weight to stones."""
        pass


# Adapter Implementation
class WeightMachineAdapter(IWeightMachineAdapter):
    """Concrete implementation of the adapter."""
    def __init__(self, weight_machine: IWeightMachine):
        self.weight_machine = weight_machine

    def get_weight_in_kilograms(self):
        """Convert weight to kilograms."""
        weight_in_pounds = self.weight_machine.get_weight_in_pounds()
        return round(weight_in_pounds * 0.453592, 2)

    def get_weight_in_stones(self):
        """Convert weight to stones."""
        weight_in_pounds = self.weight_machine.get_weight_in_pounds()
        return round(weight_in_pounds * 0.0714286, 2)


# Client Code
if __name__ == "__main__":
    # Adaptee
    weight_machine = WeightMachine()

    # Adapter
    adapter = WeightMachineAdapter(weight_machine)

    # Default weight in pounds
    print(f"Weight in pounds: {weight_machine.get_weight_in_pounds()} lbs")

    # Converted weights
    print(f"Weight in kilograms: {adapter.get_weight_in_kilograms()} kg")
    print(f"Weight in stones: {adapter.get_weight_in_stones()} st")
