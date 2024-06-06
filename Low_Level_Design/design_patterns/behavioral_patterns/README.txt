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