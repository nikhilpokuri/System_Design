from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def description(self):
        pass

class BasicCoffee(Coffee):
    def price(self):
        return 20
    def description(self):
        return "Simple Coffee"

class CoffeeDecorator:
    def __init__(self, coffee:Coffee):
        self.coffee = coffee

    @abstractmethod
    def price(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

class MilkDecorator(CoffeeDecorator):
    def price(self):
        return self.coffee.price() + 2
    
    def description(self):
        return self.coffee.description() + " with Milk"

class CreamDecorator(CoffeeDecorator):
    def price(self):
        return self.coffee.price() + 1
    
    def description(self):
        return self.coffee.description() + ", Cream"

my_coffee = BasicCoffee()
print(my_coffee.price())
print(my_coffee.description())

print()

my_coffee = MilkDecorator(my_coffee)
print(my_coffee.price())
print(my_coffee.description())

print()

my_coffee = CreamDecorator(my_coffee)
print(my_coffee.price())
print(my_coffee.description())
