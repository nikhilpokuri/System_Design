from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    """
    Interface for building the house
    """
    def __init__(self):
        self.house = ConstructHouse()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    def get_house(self):
        return self.house

class ConstructHouse:
    """
    configurations required for building the house
    """
    def __init__(self):
        self.__walls = None
        self.__roof = None
        self.__windows = None
    
    def set_walls(self,walls):
        self.__walls = walls
    
    def set_roof(self,roof):
        self.__roof = roof

    def set_windows(self,windows):
        self.__windows = windows
    
    def __str__(self):
        return f'House Properties:\n {self.__walls} walls\n {self.__roof} roof\n {self.__windows} windows'

class WoodenBuilder(HouseBuilder):
    """
    concrete implementation of HouseBuilder, 
    construction logic seprated from the configurations
    """
    def build_roof(self):
        self.house.set_roof('Shinge')
        return self
    
    def build_walls(self):
        self.house.set_walls('Wood')
        return self
    
    def build_windows(self):
        self.house.set_windows('Single Pane')
        return self

class BrickBuilder(HouseBuilder):
    """
    concrete implementation of HouseBuilder, 
    construction logic seprated from the configurations
    """
    def build_roof(self):
        self.house.set_roof('Tile')
        return self
    
    def build_walls(self):
        self.house.set_walls('Brick')
        return self
    
    def build_windows(self):
        self.house.set_windows('Double Glazed')
        return self


class Builder:
    """
    Acts as a Director, when you dont have any customizations in configuring
    """
    def __init__(self, builder:HouseBuilder):
        self.builder = builder
    
    def construct_house(self):
        return (self.builder.
                build_roof().
                build_walls().
                build_windows().
                get_house())
#client
print(Builder(WoodenBuilder()).construct_house()) #encapsulated construction witth Builder
print(BrickBuilder().build_roof().build_walls().build_windows().get_house()) #directly accessing Without Builder