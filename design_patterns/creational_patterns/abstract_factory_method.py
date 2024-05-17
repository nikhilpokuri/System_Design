from abc import ABC, abstractmethod

"""
Abstract Products: 
    Engine and Wheels define interfaces for the products.
"""
class Engine(ABC):
    @abstractmethod
    def engine_model(self):
        pass

class Wheels(ABC):
    @abstractmethod
    def wheels_count(self):
        pass

"""
Concrete Products: 
    CarEngine, CarWheels and BusEngine, BusWheels are the implementations.
"""
class CarEngine(Engine):
    def engine_model(self):
        model = 'Ferrari 3.9-litre twin-turbo V8'
        return f'Engine: {model}'
    
class CarWheels(Wheels):
    def wheels_count(self):
        count = 4
        return f'wheels: {count}'

#concrete classes for bus
class BusEngine(Engine):
    def engine_model(self):
        model = 'WP2.3 series bus engine'
        return f'Engine: {model}'
    
class BusWheels(Wheels):
    def wheels_count(self):
        count = 6
        return f'wheels: {count}'

#
class AbstractVehicleFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_wheels(self):
        pass
    
    @abstractmethod
    def vehicle_type(self):
        pass

"""
Abstract Factory: 
    AbstractVehicleFactory defines the interface for creating a family of products.
"""
class CarFactory(AbstractVehicleFactory):
    def create_engine(self):
        return CarEngine()
    
    def create_wheels(self):
        return CarWheels()

    def vehicle_type(self):
        _type = 'CAR'
        return f'Vehicle: {_type}'

class BusFactory(AbstractVehicleFactory):
    def create_engine(self):
        return BusEngine()
    
    def create_wheels(self):
        return BusWheels()
    
    def vehicle_type(self):
        _type = 'BUS'
        return f'Vehicle: {_type}'

"""
Client Code: 
    The client code uses the factories to create and interact
      with the products without knowing their concrete classes.
"""
def client(factory: AbstractVehicleFactory):
    engine = factory.create_engine()
    wheels = factory.create_wheels()
    vehicle = factory.vehicle_type()
    print('___Vehicle Was Created With Following Specifications__')
    print(f'{vehicle}')
    print(engine.engine_model())
    print(wheels.wheels_count())

client(CarFactory())
print()
client(BusFactory())
