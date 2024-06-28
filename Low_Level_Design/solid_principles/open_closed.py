"""
open-closed
- open for extension
- close for modification
"""
# if we include another payment type, 
# we have to change the code in the class which violates open-closed principle
class Payment:
    def pay(self, payment_type, amount):
        if payment_type == "credit":
            return f"{amount} paid with credit card"
        if payment_type == "upi":
            return f"{amount} paid with upi"
        if payment_type == "debit":
            return f"{amount} paid with debit"
# ---------------------------------------------------------

# we have created PaymentType interface to achieve open-closed princile
# now, our class is close for modification, open for extension
from abc import ABC, abstractmethod

class PaymentType(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Credit(PaymentType):
    def pay(self, amount):
        return f"{amount} paid with credit card"
    
class Upi(PaymentType):
    def pay(self, amount):
        return f"{amount} paid with upi card"

class Debit(PaymentType):
    def pay(self, amount):
        return f"{amount} paid with debit card"