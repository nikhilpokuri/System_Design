from abc import ABC, abstractmethod

class Engine(ABC):
    """
    interface for installing vehicle engine with engine_model method
    """
    @abstractmethod
    def engine_model(self):
        pass

class Wheels(ABC):
    """
    interface for installing vehicle wheels with wheels_count method
    """
    @abstractmethod
    def wheels_count(self):
        pass

#concrete classes for car
class CarEngine(Engine):
    """
    concrete implementation of Engine Interface
    """
    def engine_model(self):
        model = 'Ferrari 3.9-litre twin-turbo V8'
        return f'Engine: {model}'
    
class CarWheels(Wheels):
    """
    concrete implementation of Wheels Interface
    """
    def wheels_count(self):
        count = 4
        return f'wheels: {count}'

#concrete classes for bus
class BusEngine(Engine):
    """
    concrete implementation of Engine Interface
    """
    def engine_model(self):
        model = 'WP2.3 series bus engine'
        return f'Engine: {model}'
    
class BusWheels(Wheels):
    """
    concrete implementation of Wheels Interface
    """
    def wheels_count(self):
        count = 6
        return f'wheels: {count}'

#
class AbstractVehicleFactory(ABC):
    """
    interface for creating a family of products
    """
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_wheels(self):
        pass
    
    @abstractmethod
    def vehicle_type(self):
        pass

class CarFactory(AbstractVehicleFactory):
    """
    concrete implementations of AbstractVehicleFactory to create specific car products
    """
    def create_engine(self):
        return CarEngine()
    
    def create_wheels(self):
        return CarWheels()

    def vehicle_type(self):
        _type = 'CAR'
        return f'Vehicle: {_type}'

class BusFactory(AbstractVehicleFactory):
    """
    concrete implementations of AbstractVehicleFactory to create specific bus products
    """
    def create_engine(self):
        return BusEngine()
    
    def create_wheels(self):
        return BusWheels()
    
    def vehicle_type(self):
        _type = 'BUS'
        return f'Vehicle: {_type}'


def factory(factory: AbstractVehicleFactory):
    """
    The client code uses the factories to create and interact
    with the products without knowing their concrete classes.
    """
    engine = factory.create_engine()
    wheels = factory.create_wheels()
    vehicle = factory.vehicle_type()
    print('___Vehicle Was Created With Following Specifications__')
    print(f'{vehicle}')
    print(engine.engine_model())
    print(wheels.wheels_count())

#client
factory(CarFactory())
print()
factory(BusFactory())
