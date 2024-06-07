from abc import ABC, abstractmethod
import time

class FoodSystem(ABC):
    """Template Class"""

    def availability(self, order):
        print(f"(FoodSYSTEM): {order} is available")

    @abstractmethod
    def accept_order(self, order):
        pass
    
    @abstractmethod
    def specifications(self, specifications:list):
        pass

    @abstractmethod
    def cooking_status(self):
        """added sleep to wait for order preparation"""
        pass
    
    def serve(self, order):
        print(f"(FoodSYSTEM): serving {order}")
    
    def template(self, order, specifications:list=[]):
        """template method"""
        self.availability(order)
        if specifications:
            self.specifications(specifications)
        self.accept_order(order)
        self.cooking_status(order)
        self.serve(order)

class Breakfast(FoodSystem):
    """Concrete Class for Breakfast"""
    def specifications(self, specifications: list):
        print(f"(FoodSYSTEM): {specifications} added to your dish")

    def accept_order(self, order):
        print(f"(FoodSYSTEM): breakfast order {order} accepted")
    
    def cooking_status(self, order):
        print(f"(FoodSYSTEM): {order} preparing")
        time.sleep(1)
        print(f"(FoodSYSTEM): {order} preparing")
        time.sleep(1)
        print(f"(FoodSYSTEM): {order} prepared")
        time.sleep(0.5)
   
class Meals(FoodSystem):
    """Concrete Class for Meals"""
    def specifications(self, specifications: list):
        print(f"(FoodSYSTEM): {specifications} added on PIZZA")

    def accept_order(self, order):
        print(f"(FoodSYSTEM): Meals order {order} accepted")
    
    def cooking_status(self, order):
        print(f"(FoodSYSTEM): {order} preparing")
        time.sleep(2)
        print(f"(FoodSYSTEM): {order} preparing")
        time.sleep(1)
        print(f"(FoodSYSTEM): {order} prepared")
        time.sleep(0.5)

order1 = Breakfast()
order1.template("Dosa", ["onions", "chilli"])

print()

order2 = Meals()
order2.template("SambarRice")