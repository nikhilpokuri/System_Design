ABSTRACT FACTORY METHOD
    USECASE:
     - To create multiple, related objects that belong together and ensure that they are used together.
        here, Engine and Wheels
     - To abstract the creation of complex object families 
        and provide an interface for creating those objects 
        without specifying their concrete classes

    Abstract Products: 
        Engine and Wheels define interfaces for the products.
    Concrete Products: 
        CarEngine, CarWheels and BusEngine, BusWheels are concrete implementations of Engine and Wheels interfaces.

    Abstract Factory: 
        AbstractVehicleFactory defines the interface for creating a family of products.
    Concrete Factories: 
        CarFactory and BusFactory implement AbstractVehicleFactory to create specific products.

    Client Code: 
        The client code uses the factories to create and interact
        with the products without knowing their concrete classes.
------------------------------------------------------------------------------------------------   
Factory Method Pattern
    USECASE:
        To create one type of product or object here, Only Payment Product

    Abstract Product:
        Payment defines an interface for making payments with a pay method.
    Concrete Products:
        GooglePayPayment, PhonePePayment, and PaytmPayment are concrete implementations of the Payment interface.
    
    Factory Method Base Class:
        PaymentFactory function acts as a factory method to create the appropriate Payment object based on the payment type.
    Concrete Factories:
        There aren't distinct concrete factory classes here since the factory method is implemented as a function (PaymentFactory). 
        However, the function serves the role of determining and instantiating the correct concrete product.
    
    Client Code:
        The client code uses the PaymentFactory function to create and interact with different Payment objects without needing to know their specific classes.
-------------------------------------------------------------------------------------------------
Prototype Pattern Structure
    USECASE:
        - To create duplicate objects while ensuring performance.
        - When the cost of creating a new object is more expensive than cloning an existing one.
    
    Abstract Product:
        Person is the prototype interface.
    Concrete Products:
        Teacher and Student are concrete implementations of person interface.
    
    Client:
        Uses the clone method to duplicate existing objects instead of creating new ones from scratch.
        The client in this case demonstrates cloning and modifying objects.
-------------------------------------------------------------------------------------------------
Fluent Builder Pattern
    USECASE:
        - To create the complex objects step by step and separate the construction process
          and optional configurations
        - Use this pattern when you have multiple products

    Abstract Product:
        - HouseBuilder is an abstract class with abstract methods build_walls, build_roof, and build_windows.
        - It initializes a ConstructHouse object and has a method get_house to return the constructed house.
    Concrete Builders:
        - WoodenBuilder and BrickBuilder are concrete implementations of HouseBuilder.
            WoodenBuilder sets the walls, roof, and windows to wood, shingle, and single pane.
            BrickBuilder sets the walls, roof, and windows to brick, tile, and double-glazed.
    Product:
        - ConstructHouse is the product class that has methods to set its properties (walls, roof, windows).
        - The __str__ method provides a string representation of the house properties.
    
    Director (Optional):
        The Builder class can be considered a director.
        that manages the construction process using a specific builder without customizing configurations.
    
    Client Code:
        - The client code demonstrates how to use the builders to construct houses.
        - Use Builder as a director if you dont have Optional configurations.
        - Or build objects step by step without Builder when you have Optional configurations.

Builder Pattern:
    USECASE:
        - To create the complex objects step by step and separate the construction process.
        - To allow the customizing configurations by providing that particular object.
    Product:
        HouseBuilder is the construction process which takes the instance of House and set the values
    
    client:
        creates the objects step by step construction and incase of customizing or missing configurations

Singleton Pattern:
    USECASE:
        - To restrict the creation of instances more than one.
    DB_Connection:
        - Class for creation of Database Connection (say).
        - Since creation of multiple instances may occur more costs, so restricting to one object.
    get_instance:
        - It is a staticmethod which belongs to class not instance.
        - Created to return the instance when requested.
        - If this method call's for another time, return the previous instance.
        - This will not throw error, because this is staticmethod, 
          we don't have to create object again to call this method.