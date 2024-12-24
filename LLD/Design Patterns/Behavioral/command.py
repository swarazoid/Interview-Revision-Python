"""
Use case: This design pattern is particularly useful when implementing undo/redo mechanisms, as each command can store its state for reversal.
This pattern helps decouple the sender (Invoker) from the receiver, making the system more modular and easier to extend. Otherwise the Invoker class(client) will be directly coupled with the AirConditioner class which is not good for scaling.

So we introduce command concrete classes between Invoker and reciever. Each command can implement its undo function too.
"""

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class AirConditioner:
    def __init__(self):
        self.temperature = 24

    def increase_temperature(self):
        self.temperature += 1
        print(f"Temperature increased to {self.temperature}°C")

    def decrease_temperature(self):
        self.temperature -= 1
        print(f"Temperature decreased to {self.temperature}°C")

# Concrete Commands
class IncreaseTemperatureCommand(Command):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.increase_temperature()

    def undo(self):
        self.ac.decrease_temperature()

class DecreaseTemperatureCommand(Command):
    def __init__(self, ac: AirConditioner):
        self.ac = ac

    def execute(self):
        self.ac.decrease_temperature()

    def undo(self):
        self.ac.increase_temperature()

# Invoker
class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command: Command):
        command.execute()
        self.history.append(command)

    def press_undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("No commands to undo.")

# Client Code
if __name__ == "__main__":
    ac = AirConditioner()
    remote = RemoteControl()

    increase_temp_command = IncreaseTemperatureCommand(ac)
    decrease_temp_command = DecreaseTemperatureCommand(ac)

    # Simulate remote control actions
    remote.press_button(increase_temp_command)  # Temperature increased to 25°C
    remote.press_button(increase_temp_command)  # Temperature increased to 26°C
    remote.press_button(decrease_temp_command)  # Temperature decreased to 25°C

    # Undo last actions
    remote.press_undo()  # Temperature increased to 26°C
    remote.press_undo()  # Temperature decreased to 25°C
    remote.press_undo()  # Temperature decreased to 24°C
    remote.press_undo()  # No commands to undo.
