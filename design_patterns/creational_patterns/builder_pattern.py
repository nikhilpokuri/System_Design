class House:
    def __init__(self) -> None:
        self._type = None
        self._material = None
        self._floors = None

    def __str__(self) -> str:
        return f'House Details\n Type: {self._type}\n Material: {self._material}\n Floors: {self._floors}'

class HouseBuilder:
    def __init__(self, house=House()) -> None:
        self.house = house

    def set_type(self, type):
        self.house._type = type
        return self
    
    def set_material(self, material):
        self.house._material = material
        return self
    
    def set_floors(self, floors):
        self.house._floors = floors
        return self
    
    def build_home(self):
        return self.house

#client
house1 = (HouseBuilder(House()).
         set_type('duplex').
         set_material('iron').
         build_home()
         ) #missed passing floors

house2 = (HouseBuilder(House()).
        set_type('stairs').
        set_floors(4).
        build_home()
        ) #missed passing material

#pass the missing configurations or update using the particular object
HouseBuilder(house1).set_floors(2).set_material('brick')
HouseBuilder(house2).set_material('wood')

print(house1, '\n')
print(house2)
