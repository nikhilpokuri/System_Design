Adapter Pattern:
    USECASE:
        - To enable classes with incompatible interfaces to work together.
        - To use an existing class but its interface does not match the one you need.
    
    Abstract Target:
        DataReader is abstract class defines the read_data method that all concrete adapters must implement.
    
    Adaptees:
        [ JSONReader, XMLReader, CSVReader ]
        different interfaces that need to be adapted to the target interface.
    Adapter:
        [ DataReaderAdapter ]
        Adapts the interfaces of the adaptees to the target interface.
    
    Client:
        [ load_data function ]
        Uses the adapter to read data from different file types without worrying about their specific implementations.

Bridge Pattern:
    USECASE:
        - To avoid the creation of multiple classes.
        - To separate the abstraction from its implementation so that both can be modified independently.
    
    Abstract Implementor:
        [ Device ]
        Defines the interface for different types of devices that can be controlled.
    Concrete Implementors:
        [ Radio, Television]
        Implement the Device interface and provide specific behaviors for different device types.

      ex :- If we add more devices like Speaker, HomeTheater
         WITHOUT BRIDGE PATTERN:
            - we have to create the classes with same methods volume_up(), volume_down() for both
         WITH BRIDGE PATTERN:
            - we simply create the device concrete implementors for both
    Client:
        The client code uses the BasicRemote to control the volume of different devices 
        (Radio, Television, HomeTheater, Speaker).