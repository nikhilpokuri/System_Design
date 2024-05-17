from abc import ABC, abstractmethod

class Payment(ABC):
    """
    interface for making payments with a pay method
    """
    @abstractmethod
    def pay(self, amount):
        pass

class GooglePayPayment(Payment):
    """
    concrete implementations of the Payment interface
    """
    def pay(self, amount):
        return f"Payment {amount} Done Using  GooglePay"

class PhonePePayment(Payment):
    """
    concrete implementations of the Payment interface
    """
    def pay(self, amount):
        return f"Payment {amount} Done Using  GooglePay"

class PaytmPayment(Payment):
    """
    concrete implementations of the Payment interface
    """
    def pay(self, amount):
        return f"Payment {amount} Done Using  GooglePay"

#we can keep create factory using class also
def PaymentFactory(payment_type):
    """
    factory method to create the appropriate Payment object based on the payment type
    """
    factory = {
        "phonepe": PhonePePayment,
        "googlepay": GooglePayPayment,
        "paytm": PaytmPayment
    }
    if payment_type in factory:
        return factory[payment_type]()
    else:
        raise ValueError(f'{payment_type} is not available')
#client
mode = PaymentFactory("googlepay") #phonepe, googlepay, paytm
print(mode.pay(1000))