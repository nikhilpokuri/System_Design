""" 
Interface segregation: No sub-class should be forced to depend on it's supercalss methods
                       which is non related to it. 
"""
# we are forcing all subclasses to use twoStepAuthentication even if it not needed like Zoom..
# So we are violating Interface segregation principle

from abc import ABC, abstractmethod

class LoginProcessor(ABC):
    @abstractmethod
    def login(self, mail, password):
        pass

    @abstractmethod
    def twoStepAuthentication(self):
        pass

class Gmail(LoginProcessor):
    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR]: Please Verify that it's you.!!")
        return self.twoStepAuthentication()
    
    def twoStepAuthentication(self):
        print("[TWO STEP AUTHENTICATOR]: Authentication Successfull")
        return "Gmail Logged In\n"

class Facebook(LoginProcessor):
    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR]: Please Verify that it's you.!!")
        return self.twoStepAuthentication()
    
    def twoStepAuthentication(self):
        print("[TWO STEP AUTHENTICATOR]: Authentication Successfull")
        return "Facebook Logged In\n"
    
class Zoom(LoginProcessor):
    def login(self, mail, password):
        return f"{self.twoStepAuthentication()}\nZoom Logged In\n"
    
    def twoStepAuthentication(self):
        return "[TWO STEP AUTHENTICATOR]: Two Step Authentication Not Needed"

mail = Gmail()
facebook = Facebook()
zoom = Zoom()
print(mail.login("nick@gmail.com", "password"))
print(facebook.login("nick@gmail.com", "password"))
print(zoom.login("nick@gmail.com", "password"))
print()
# ---------------------------------------------------------

# Below, we have separated the Authenticator from LoginProcessor to achieve Interface segregation.
# But we are depending on another class, 
# this violates Dependency Inversion Principle, we'll achieve Dependency Inversion in dependency_inversion.py

class LoginProcessor(ABC):
    @abstractmethod
    def login(self, mail, password):
        pass

class Authenticator:
    def twoStepAuthentication(self):
        print("[TWO STEP AUTHENTICATOR]: Authentication Successfull")

class Gmail(LoginProcessor):
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR]: Please Verify that it's you.!!")
        self.authenticator.twoStepAuthentication()
        return "Gmail Logged In\n"

class Facebook(LoginProcessor):
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR]: Please Verify that it's you.!!")
        self.authenticator.twoStepAuthentication()
        return "Facebook Logged In\n"

class Zoom(LoginProcessor):
    def login(self, mail, password):
        return "Zoom Logged In\n"

mail = Gmail(Authenticator())
facebook = Facebook(Authenticator())
zoom = Zoom()
print(mail.login("nick@gmail.com", "password"))
print(facebook.login("nick@gmail.com", "password"))
print(zoom.login("nick@gmail.com", "password"))