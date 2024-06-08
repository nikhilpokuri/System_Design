from __future__ import annotations

from abc import ABC, abstractmethod


class AnimalVisitor(ABC):
    """Abstract Visitor Class"""

    @abstractmethod
    def visit_racoon(self, racoon: Animal):
        pass

    @abstractmethod
    def visit_wolf(self, wolf: Animal):
        pass

class FoodVisitor(AnimalVisitor):
    """Concrete Visitor Class"""

    def visit_racoon(self, racoon: Animal):
        print(f"Feeding Racoon {racoon.name}")
    
    def visit_wolf(self, wolf: Animal):
        print(f"Feeding Wolf {wolf.name}")

class CleanVisitor(AnimalVisitor):
    """Concrete Visitor Class"""

    def visit_racoon(self, racoon: Animal):
        print(f"Cleaning Racoon {racoon.name}")
    
    def visit_wolf(self, wolf: Animal):
        print(f"Cleaning Wolf {wolf.name}")


class Animal(ABC):
    """Abstract Element/Visitable Class"""

    @abstractmethod
    def accept(self, visitor):
        pass

class Racoon(Animal):
    """Concrete Element/Visitable Class"""

    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor:AnimalVisitor):
        visitor.visit_racoon(self)

class Wolf(Animal):
    """Concrete Element/Visitable Class"""

    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor:AnimalVisitor):
        visitor.visit_wolf(self)

class Zoo:
    """Object Structure To Collect All Animal Objects"""
    def __init__(self):
        self.__animals = []
    
    def add_animal(self, animal:Animal):
        self.__animals.append(animal)

    def perform_visit(self, visitor:AnimalVisitor):
        for animal in self.__animals:
            animal.accept(visitor)


racoon = Racoon("doraemon")
wolf = Wolf("john")
zoo = Zoo()

zoo.add_animal(racoon)
zoo.add_animal(wolf)

zoo.perform_visit(FoodVisitor())
print()
zoo.perform_visit(CleanVisitor())