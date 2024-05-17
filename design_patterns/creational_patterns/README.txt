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
     - To create one type of product or object
       here, Only Payment Product
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