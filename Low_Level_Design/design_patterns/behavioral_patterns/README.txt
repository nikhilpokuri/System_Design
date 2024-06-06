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