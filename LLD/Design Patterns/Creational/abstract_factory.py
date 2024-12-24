"""
Use case: This is used when we have multiple factories. So we create factory of factories.
Example 1:
Assume we have 2 types of cars: Luxury cars and Ordinary cars. Ths will be first factory
within each there can be multiple cars, so this will be another factory

Example 2:
Assume we have room decoration themes, like modern, antique. This will be the first factory
Within each we will have different design of chair, tables, sofas etc. This will be the second factory
"""

# sample use case: Get price of furnitures for different themes

from abc import ABC, abstractmethod

class Furniture(ABC):
    @abstractmethod
    def get_cost():
        pass

class AntiqueChair(Furniture):
    def get_cost(self):
        return "Rs. 550"
    
class AntiqueTable(Furniture):
    def get_cost(self):
        return "Rs. 820"
    
class ModernChair(Furniture):
    def get_cost(self):
        return "Rs. 250"
    
class ModernTable(Furniture):
    def get_cost(self):
        return "Rs. 460"
    
class ThemedFurnituresInterface(ABC):
    @abstractmethod
    def get_furniture(self, furniture):
        pass

class AntiqueFurntures(ThemedFurnituresInterface):
    def get_furniture(self, furniture):
        if furniture == "chair":
            return AntiqueChair()
        elif furniture == "table":
            return AntiqueTable()
        
class ModernFurntures(ThemedFurnituresInterface):
    def get_furniture(self, furniture):
        if furniture == "chair":
            return ModernChair()
        elif furniture == "table":
            return ModernTable()
    
class ThemeFactoryInterface(ABC):
    @abstractmethod
    def get_themed_furnitures(self, theme):
        pass

class ThemeFactory(ThemeFactoryInterface):
    def get_themed_furnitures(self, theme):
        if theme == "antique":
            return AntiqueFurntures()
        elif theme == "modern":
            return ModernFurntures()
        

if __name__ == "__main__":
    theme_factory = ThemeFactory()

    antique_furnitures = theme_factory.get_themed_furnitures("antique")
    print(antique_furnitures.get_furniture("chair").get_cost())
    print(antique_furnitures.get_furniture("table").get_cost())

    modern_furnitures = theme_factory.get_themed_furnitures("modern")
    print(modern_furnitures.get_furniture("chair").get_cost())
    print(modern_furnitures.get_furniture("table").get_cost())
    

