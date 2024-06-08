                            BEHAVIORAL DESIGN PATTERNS

Chain of Responsibility Pattern:
    USECASE:
        - To decouple the sender of a request from its receiver by giving multiple objects a chance to handle the request.
        - To pass the request along a chain of potential handlers until it is processed.
    
    Abstract Handler:
        [ ExpenseHandler ]
        - This is an abstract class that defines a handle_expense method which all concrete handlers must implement. 
        - It maintains a reference to the next handler in the chain.
    
    Concrete Handlers:
        [ SupervisorHandler, ManagerHandler, CeoHandler, FounderHandler ]
        - SupervisorHandler: If the amount exceeds this 1000, it passes the request to the next handler.
        - ManagerHandler: If the amount exceeds this 5000, it passes the request to the next handler.
        - CeoHandler: If the amount exceeds this 10000, it passes the request to the next handler.
        - FounderHandler: If the amount exceeds this 100000, it passes the request to the next handler or rejects it if there is no handler available.
    
    Client:
        - Client code calls expense_handler function and sends various expense amounts which passes through the chain. 
        - The request is processed by the appropriate handler, ensuring that the expense approval logic is encapsulated within the handler classes.

-------------------------------------------------------------------------------------------------

Command Pattern:
    USECASE:
        - To encapsulate a request as an object with queues which may help in async execution.
        - To support undoable operations.

    Abstract Command:
        [ Command ]
        Defines an execute method, which all concrete command classes must implement.
    
    Concrete Commands:
        [ SignupNotificationCommand, LoginNotificationCommand, LogoutNotificationCommand ]
        - SignupNotificationCommand: Implements the execute method to send a signup notification by calling the appropriate method on the receiver.
        - LoginNotificationCommand: Implements the execute method to send a login notification by calling the appropriate method on the receiver.
        - LogoutNotificationCommand: Implements the execute method to send a logout notification by calling the appropriate method on the receiver.
    
    Receiver:
        [ NotificationService ]
        Contains the business logic to send different types of notifications (signup, login, logout).

    Invoker:
        [ NotificationInvoker ]
        Maintains a list of commands and can add commands, undo the last command, and perform all added commands.
    
    Client:
        Creates concrete command objects and use the invoker to add and execute them.

-------------------------------------------------------------------------------------------------

Interpreter Pattern:
    USECASE:
        - To define a grammatical representation for a language and provide an interpreter to deal with this grammar.
        - To interpret sentences in a language by breaking them down into expressions.
          eg:- (10 * 20) - (10 + 20)
    
    Abstract Expression:
        [ Expression ]
        Defines the interpret method, which all concrete expression classes must implement.
    
    Terminal Expression:
        [ Number ]
        - Represents the terminal symbols in the grammar. 
        - It holds a number and simply returns its value when the interpret method is called.
    
    Non-Terminal Expressions:
        [ Add, Subtract, Multiply, Divide ]
        - Add: Represents the addition operation and interprets the sum of its left and right sub-expressions.
        - Subtract: Represents the subtraction operation and interprets the difference of its left and right sub-expressions.
        - Multiply: Represents the multiplication operation and interprets the product of its left and right sub-expressions.
        - Divide: Represents the division operation and interprets the quotient of its left and right sub-expressions.
    
    Client:
        Demonstrates how to create and evaluate complex expressions using the classes defined above.

-------------------------------------------------------------------------------------------------

Iterator Pattern:
    USECASE:
        - To provide a way to access the elements sequentially without exposing its underlying representation.
        - To allow multiple traversal algorithms over a collection without modifying the collection itself.
    
    Abstract Iterator:
        [ Iterator ]
        Defines the has_next and next methods that all concrete iterators must implement.
    
    Abstract Aggregate:
        [ Aggregate ]
        Defines the add_element and create_iterator methods that all concrete aggregates must implement.
    
    Concrete Iterator:
        [ ListIterator ]
        - Implements the Iterator interface to iterate over a collection. 
        - It keeps track of the current position in the collection.
    
    Concrete Aggregate:
        [ NumberCollection ]
        - Implements the Aggregate interface and provides the necessary methods to add elements to the collection
        - create_iterator: for normal traversal 
          reverse_collection: for reverse traversal.

    Client:
        Demonstrates how to use the NumberCollection and ListIterator 
        to traverse or reverse traverse and access the elements of the collection.

-------------------------------------------------------------------------------------------------

Memento Pattern:
    USECASE:
        - To capture and store the current state of an object so that it can be restored later without violating encapsulation.
        - To provide undo functionality or to save and restore to desired state of an object.

    Memento
    [ EditorMemento ]
        - Stores the state/saved-data of the Originator.
        - Provides a method to retrieve the stored state.

    Originator
    [ TextEditor ]
        - Maintains the state of the text.
        - Provides methods to write text, save its current state, and restore to memento desired state.

    Caretaker
    [ EditorHistory ]
        - Manages the mementos.
        - Responsible for saving originator's state
            restoring to previous Originator's state using the Memento.

-------------------------------------------------------------------------------------------------

Strategy Pattern:
    USECASE:
        - To define a group of algorithms, encapsulate each one, and make them interchangeable.
        - To allow the algorithm to vary independently from clients that use it.

    Context:
        [ Transport ]
        - This class is configured with a strategy object.
        - It maintains a reference to a strategy object and execute.

    Strategies:
        [ airTransport, roadTransport, waterTransport ]
        - Strategies implementing the algorithm using different means of transport.

    Client:
        - The client creates a context and configures it with one of the strategies.
        - It interacts with the context to execute the strategy.

-------------------------------------------------------------------------------------------------
   
Template Method Pattern:
    USECASE:
        - To define the skeleton of an algorithm in a base class 
          and allow subclasses to redefine specific steps of the algorithm without changing its structure.
        - Don't have to call the each and every step, just call the template method

    Template Class:
        [ FoodSystem ]
        - Template method template which provides the skeleton of the food ordering process.
        - Includes abstract methods [ accept_order, specifications, cooking_status ] that subclasses must implement.
        - Contains a concrete methods [ availability, serve ].
    
    Concrete Classes:
        [ Breakfast, Meals ]
        Breakfast:
            - Implements accept_order, specifications, and cooking_status for breakfast orders.
            - Specifies how to handle breakfast-specific order steps.
        Meals:
            - Implements accept_order, specifications, and cooking_status for meal orders.
            - Specifies how to handle meal-specific order steps.
    
    Client:
        - Client creates instances of Breakfast and Meals.
        - Calls the template method on these instances to execute the algorithm with different implementations of the steps.

-------------------------------------------------------------------------------------------------

Observer Pattern:
    USECASE:
    - To establish a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically.
    - Useful when changes to one object require notifying and updating a varying number of other objects.
    
    Abstract Observer:
    [ Observer ]
    - Defines an abstract method set_temperature that all concrete observers must implement.

    Subject:
        [ WeatherStation ]
        - Maintains a list of observers and provides methods to subscribe and unsubscribe observers.
        - Method (notify_all) Notifies all subscribed observers of temperature changes by calling their set_temperature method.

    Concrete Observers:
        [ AirConditionerObserver, GeyserObserver ]
        - Implement the Observer interface and define the set_temperature method to update their state based on the subject's state.
        - AirConditionerObserver: Responds to temperature changes by turning the air conditioner on or off.
        - GeyserObserver: Responds to temperature changes by turning the geyser on or off.

    Client:
        - Creates instances of the subject (WeatherStation) and concrete observers (AirConditionerObserver, GeyserObserver).
        - Subscribes and Unsubscribes observers to the subject.
        - Notifies all observers of state changes by calling the notify_all method on the subject.

-------------------------------------------------------------------------------------------------

Visitor Pattern:
    USECASE:
        - To define new operations without changing the classes of elements/Visitables on which they operate.
        - Useful when you have a complex object structure and need to perform different kinds of operations on these objects.
    
    Abstract Visitor:
    [ AnimalVisitor ]
        - Declares visit methods for each type of concrete element (visit_racoon and visit_wolf) that all concrete visitors must implement.
    
    Concrete Visitors:
    [ FoodVisitor, CleanVisitor ]
        - Implement the visit methods (visit_racoon and visit_wolf) to define specific operations for each element.
        - FoodVisitor: Implements feeding operations for racoon and wolf.
        - CleanVisitor: Implements cleaning operations for racoon and wolf.
    
    Abstract Element/Visitable:
    [ Animal ]
        - Declares an accept method that takes a visitor object, which concrete elements must implement.
    
    Concrete Elements/Visitable:
    [ Racoon, Wolf ]
        - Implement the accept method to call the appropriate visit method on the visitor.
        - Racoon: Implements accept method to call visit_racoon on the visitor.
        - Wolf: Implements accept method to call visit_wolf on the visitor.
    
    Object Structure:
    [ Zoo ]
        - Manages a collection of elements/visitables and allows performing operations on them using visitors.
        - Contains methods to (add_animal, perform_visit) by iterating through the animals and accepting visitors.
    
    Client:
        - Creates instances of concrete elements (Racoon, Wolf) and adds them to the Zoo.
        - Creates concrete visitors (FoodVisitor, CleanVisitor) and performs operations on the Zoo's elements by calling perform_visit.