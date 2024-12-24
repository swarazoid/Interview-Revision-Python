"""
Defintion: Bridge pattern decouples an abstraction from its implementation so that they can vary independently.
Explanation:
In the below class we can see now that since we have separated the BreathingTechnique and LivingThings, concrete implementations of both can vary independently. A new breathing technique isn't neceesarily to be tied to a living thing yet.
"""

# sample use case: Implement a class based on living things breathing styles

from abc import ABC, abstractmethod

# Abstract Implementor
class BreathingTechnique(ABC):
    @abstractmethod
    def breathe(self):
        pass


# Concrete Implementors
class LungsBreathing(BreathingTechnique):
    def breathe(self):
        return "breathes using lungs."


class GillsBreathing(BreathingTechnique):
    def breathe(self):
        return "breathes using gills."


class SkinBreathing(BreathingTechnique):
    def breathe(self):
        return "breathes through its skin."


# Abstraction (LivingThings)
class LivingThings:
    def __init__(self, name, breathing_technique: BreathingTechnique):
        self.name = name
        self.breathing_technique = breathing_technique

    def breathe(self):
        return f"{self.name} {self.breathing_technique.breathe()}"


# Refined Abstractions
class LandLivingThings(LivingThings):
    def __init__(self, name, breathing_technique: BreathingTechnique):
        super().__init__(name, breathing_technique)


class WaterLivingThings(LivingThings):
    def __init__(self, name, breathing_technique: BreathingTechnique):
        super().__init__(name, breathing_technique)


# Client Code
if __name__ == "__main__":
    # Land living things
    frog = LandLivingThings("Frog", SkinBreathing())
    human = LandLivingThings("Human", LungsBreathing())

    # Water living things
    fish = WaterLivingThings("Fish", GillsBreathing())
    whale = WaterLivingThings("Whale", LungsBreathing())

    print(frog.breathe())  # Frog breathes through its skin.
    print(human.breathe())  # Human breathes using lungs.
    print(fish.breathe())  # Fish breathes using gills.
    print(whale.breathe())  # Whale breathes using lungs.


"""
How is it different from strategy pattern, if we consider the BreathingTechnique to be BreathingStrategy?
- The difference is actually very minor. Both have very similar UML diagrams. The difference is mostly the intent.

Differences in Intent:
Bridge (Current Implementation): 
- Designed to decouple LivingThings from BreathingTechnique, allowing them to vary independently. You can independently extend LivingThings (e.g., add AirLivingThings) or BreathingTechnique (e.g., add TrachealBreathing) without affecting each other.
- Typically used when the abstraction and implementation have distinct hierarchies.

Strategy (Alternative Approach):
- Focused on dynamically swapping breathing techniques for a living thing during runtime.
- Doesn't inherently focus on separating abstraction and implementation but rather on providing interchangeable behaviors.

Which One to Use?
Use the Bridge Pattern when you have:
- Two separate hierarchies (abstraction and implementation).
- A need to extend both hierarchies independently.

Use the Strategy Pattern when you have:
- A single class that needs interchangeable behaviors (like dynamic breathing techniques).
- A focus on runtime flexibility.
"""