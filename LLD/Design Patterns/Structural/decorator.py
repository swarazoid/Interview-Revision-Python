"""
Use case:
Whenever we have one base class which will need many different customizations and the permuatation can be large
For example:
- Pizaa can have multiple types of toppings
- Car can have multiple types of features added
- Coffee can have multiple ratios of milk, water etc

Solution:
Create a base class.
Now create the decorator classes such that the decorator class
- has-a base class
- is-a base class
decorator class will have the same interface as base class
"""

# Sample use case: create pizza cost calculator based on the toppings added

from abc import ABC, abstractmethod

class BasePizzaInterface(ABC):
    @abstractmethod
    def calc_cost(self):
        pass

class Margherita(BasePizzaInterface):
    def __init__(self):
        self.cost = 100

    def calc_cost(self):
        return self.cost
    
class ToppingsInterface(BasePizzaInterface):
    def __init__(self, pizza):
        self.pizza = pizza
        
    @abstractmethod
    def calc_cost(self):
        pass

class CheeseTopping(ToppingsInterface):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 15
    
    def calc_cost(self):
        return self.pizza.calc_cost() + self.cost
    
class OnionTopping(ToppingsInterface):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 10
    
    def calc_cost(self):
        return self.pizza.calc_cost() + self.cost
    
if __name__ == "__main__":
    base_pizza = Margherita()
    print(base_pizza.calc_cost())

    topped_pizza = CheeseTopping(OnionTopping(CheeseTopping(base_pizza)))
    print(topped_pizza.calc_cost())
    