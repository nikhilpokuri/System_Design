from abc import ABC, abstractmethod

class ExpenseHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_expense(self, amount):
        pass

class SupervisorHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 1000:
            return f"Supervisor Approved amount of {amount}"
        elif self.next_handler:
            return self.next_handler.handle_expense(amount)
        else:
            return "Requires Higher Approval"

class ManagerHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 5000:
            return f"Manager Approved amount of {amount}"
        elif self.next_handler:
            return self.next_handler.handle_expense(amount)
        else:
            return "Requires Higher Approval"

class CeoHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 10000:
            return f"CEO Approved amount of {amount}"
        elif self.next_handler:
            return self.next_handler.handle_expense(amount)
        else:
            return "Requires Higher Approval"

class FounderHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount > 10000 and amount <= 100000:
            return f"Founder Approved amount of {amount}"
        elif self.next_handler:
            return self.next_handler.handle_expense(amount)
        else:
            return f"Founder Rejected amount of {amount}"

#client
def expense_handler(amount):
    founder = FounderHandler()
    ceo = CeoHandler(founder)
    manager = ManagerHandler(ceo)
    supervisor = SupervisorHandler(manager)

    status = supervisor.handle_expense(amount)
    return status

expenses = [1000, 1001, 3545, 10000, 10005, 100001]
for expense in expenses:
    print(expense_handler(expense))