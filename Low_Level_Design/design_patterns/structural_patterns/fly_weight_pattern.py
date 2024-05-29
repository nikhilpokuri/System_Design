class CarFlyWeight:
    def __init__(self, family, brand):
        self.family = family
        self.brand = brand
    
    def display(self, number, variant, color, max_speed):
        return f"Car {number}: {self.family} {self.brand}\nVariant: {variant}\nColor: {color}\nMax_Speed: {max_speed}\n"

class FlyWeightFactory:
    def __init__(self):
        self.factory = {}
    
    def get_flyWeight(self, family, brand):
        key = (family, brand)
        if key not in self.factory:
            self.factory[key] = CarFlyWeight(family, brand)
        return self.factory[key]

class Car:
    def __init__(self, family, brand, number, variant, color, max_speed, factory):
        self.flyWeight = factory.get_flyWeight(family, brand)
        # print(self.flyWeight) #uncomment to ensure it is re-using the objects
        self.number = number
        self.variant = variant
        self.color = color
        self.max_speed = max_speed
    
    def display(self):
        return self.flyWeight.display(self.number, self.variant, self.color, self.max_speed)

#client
fly = FlyWeightFactory()
car1 = Car("hyundai", "verna", "001", "Ex", "black", 200, fly)
car2 = Car("hyundai", "verna", "002", "S", "white", 190, fly)
car3 = Car("hyundai", "creta", "003", "E", "brown", 180, fly)
car4 = Car("hyundai", "creta", "004", "S", "white", 170, fly)
print(car1.display())
print(car2.display())
print(car3.display())
print(car4.display())