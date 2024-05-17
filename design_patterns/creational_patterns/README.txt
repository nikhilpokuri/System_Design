ABSTRACT FACTORY METHOD
    Abstract Products: 
        Engine and Wheels define interfaces for the products.
    Concrete Products: 
        CarEngine, CarWheels and BusEngine, BusWheels are the implementations.

    Abstract Factory: 
        AbstractVehicleFactory defines the interface for creating a family of products.
    Concrete Factories: 
        CarFactory and BusFactory implement AbstractVehicleFactory to create specific products.

    Client Code: 
        The client code uses the factories to create and interact
        with the products without knowing their concrete classes.