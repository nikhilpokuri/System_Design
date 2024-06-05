from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class NotificationService:
    """Bussiness Logic / Receiver Class"""

    def send_signup_notification(self, user):
        print(f"{user} Signed Up Successfully")

    def send_login_notification(self, user):
        print(f"{user} Logged In Successfully")

    def send_logout_notification(self, user):
        print(f"{user} Logged Out Successfully")


class SignupNotificationCommand(Command):
    """Command class for Signup Notification"""

    def __init__(self, user, receiver=NotificationService()):
        self.receiver = receiver
        self.user = user.capitalize()

    def execute(self):
        return self.receiver.send_signup_notification(self.user)


class LoginNotificationCommand(Command):
    """Command class for Login Notification"""

    def __init__(self, user, receiver=NotificationService()):
        self.receiver = receiver
        self.user = user.capitalize()

    def execute(self):
        return self.receiver.send_login_notification(self.user)


class LogoutNotificationCommand(Command):
    """Command class for Logout Notification"""

    def __init__(self, user, receiver=NotificationService()):
        self.receiver = receiver
        self.user = user.capitalize()

    def execute(self):
        return self.receiver.send_logout_notification(self.user)


class NotificationInvoker:
    """Invoker Class"""

    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def undo(self):
        self.commands.pop()

    def perform_commands(self):
        for command in self.commands:
            command.execute()

#client
login = LoginNotificationCommand("nick")
logout = LogoutNotificationCommand("nick")
signup = SignupNotificationCommand("nick")
invoker = NotificationInvoker()
invoker.add_command(login)
invoker.add_command(logout)
invoker.add_command(signup)
invoker.undo()
invoker.perform_commands()