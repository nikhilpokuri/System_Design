""" 
Liskov substitution:  objects of a superclass should be replaceable with objects of a subclass 
                      without affecting the functionality of a program.
"""
# Below, otp not required for cash payment, so it is not compatible with PaymentType Interface.

from abc import ABC, abstractmethod

class PaymentType(ABC):
    @abstractmethod
    def paymentProcessor(self, amount, otp):
        pass

class Credit(PaymentType):
    def paymentProcessor(self, amount, otp):
        return f"Processing credit card payment of {amount}/- with otp {otp}"

class Debit(PaymentType):
    def paymentProcessor(self, amount, otp):
        return f"Processing credit card payment of {amount}/- with otp {otp}"
    
class Cash(PaymentType):
    def paymentProcessor(self, amount, otp):
        return "[ERROR]: OTP not required for Cash payment"


credit = Credit()
debit = Debit()
cash = Cash()
print(credit.paymentProcessor(1000, 123456))
print(debit.paymentProcessor(1000, 123456))
print(cash.paymentProcessor(1000, 123456))
""" 
In this example, CashPayment violates LSP because it is 
not handling the process_payment method in a way that is compatible with the PaymentMethod class.
"""
print()

# ---------------------------------------------------------
# By designing the classes this way, we ensure that 
# all PaymentMethod subclasses handle the otp parameter correctly when needed without breaking the program.

class PaymentType(ABC):
    @abstractmethod
    def paymentProcessor(self, amount):
        pass

class Credit(PaymentType):
    def __init__(self, otp) -> None:
        self.otp = otp

    def paymentProcessor(self, amount):
        return f"Processing credit card payment of {amount}/- with otp {self.otp}"

class Debit(PaymentType):
    def __init__(self, otp) -> None:
        self.otp = otp

    def paymentProcessor(self, amount):
        return f"Processing credit card payment of {amount}/- with otp {self.otp}"
    
class Cash(PaymentType):
    def paymentProcessor(self, amount):
        return f"Processing cash payment of {amount}/-"

credit = Credit(123456)
debit = Debit(123456)
cash = Cash()
print(credit.paymentProcessor(1000))
print(debit.paymentProcessor(1000))
print(cash.paymentProcessor(1000))