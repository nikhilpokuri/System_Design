from abc import ABC, abstractmethod

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

# ---------------------------------------------------------

from abc import ABC, abstractmethod

class LoginProcessor(ABC):
    @abstractmethod
    def login(self, mail, password):
        pass

class Authenticator(ABC):
    @abstractmethod
    def twoStepAuthentication(self):
        pass

class MailAuthenticator(Authenticator):
    def twoStepAuthentication(self):
        print("[TWO STEP AUTHENTICATOR(mail)]: Authentication Successfull")

class SmsAuthenticator(Authenticator):
    def twoStepAuthentication(self):
        print("[TWO STEP AUTHENTICATOR(sms)]: Authentication Successfull")

class Gmail(LoginProcessor):
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR(mail)]: Please Verify mail that it's you.!!")
        self.authenticator.twoStepAuthentication()
        return "Gmail Logged In\n"

class Facebook(LoginProcessor):
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR(mail)]: Please Verify mail that it's you.!!")
        self.authenticator.twoStepAuthentication()
        return "Facebook Logged In\n"

class Phonepe(LoginProcessor):
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def login(self, mail, password):
        print("[TWO STEP AUTHENTICATOR(sms)]: Please Verify sms that it's you.!!")
        self.authenticator.twoStepAuthentication()
        return "Phonepe Logged In\n"

class Zoom(LoginProcessor):
    def login(self, mail, password):
        return "Zoom Logged In\n"

mail = Gmail(MailAuthenticator())
facebook = Facebook(MailAuthenticator())
phonepe = Phonepe(SmsAuthenticator())
zoom = Zoom()

print(mail.login("nick@gmail.com", "password"))
print(facebook.login("nick@gmail.com", "password"))
print(phonepe.login("nick@gmail.com", "password"))
print(zoom.login("nick@gmail.com", "password"))