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

-------------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------------

Composite Pattern:
    USECASE:
        - To represent part-whole hierarchies of objects.
        - To treat individual objects and compositions of objects uniformly.
    
    --------------------EXAMPLE-01---------------------
    Abstract Component:
        [ FileSystemComponent ]
        - Defines the interface for all components in the composition.
        - Declares a method display to display the component's details.
    Concrete Components:
        File:
            - Implements the FileSystemComponent interface.
            - Represents a leaf in the composition, i.e., an individual file.
        Directory:
            - Implements the FileSystemComponent interface.
            - Represents a composite in the composition, i.e., a directory that can contain other files or directories.
        Contains a method add_component to add files or directories.
    Client:
        - Creates a file system structure with directories and files.
        - Uses the display method to print the structure.

    -----------------------EXAMPLE-02--------------------------
    Equipment:
        Represents an individual piece of equipment with a name and price.

    Composite:
        - Represents a composite equipment item that can contain multiple pieces of equipment or other composites.
        - Contains methods to add items and calculate the total price.
    Client:
        Creates a composite structure of computer equipment and calculates the total price.

-------------------------------------------------------------------------------------------------

Decorator Pattern:
    USECASE:
        - To dynamically add responsibilities to objects.
        - To add behavior to objects at runtime without affecting other objects of the same class.
    
    Abstract Component:
        [ Coffee ] 
        Defines the price and description methods that all concrete components and decorators must implement.
    Concrete Component:
        [ BasicCoffee ]
        Implements the Coffee interface providing basic functionality.
    
    Decorator:
        [ CoffeeDecorator ] 
        contains a reference to a Coffee object and implements the Coffee interface, 
        to ensure price and description methods that all concrete decorators must implement.
    Concrete Decorators:
        [ MilkDecorator and CreamDecorator ] 
        - Extend the CoffeeDecorator and add their specific behavior to the price and description methods.
        - So that we can now customize or add responsibilities without affecting that objects
    
    Client:
        client code demonstrates how to wrap a BasicCoffee object with various decorators 
        to add different flavors and calculate the total price and description.
    
Facade Pattern:
    USECASE:
        - To encapsulate the complexities of the subsystems and provide a unified interface for the client.
    
    Subsystem Classes:
        [ VerifiedUsers, SeatAvailability, and Notification ]
        These classes perform specific functions related to the booking system.

    Facade:
        [ FacadeBooking ]
        provides a simplified interface to book a seat by combining all subsystem classes.
    
    Client:
        Client interacts with the booking system through the facade, 
        Thus, simplifying its code and reducing the need to understand the subsystem's complexity.