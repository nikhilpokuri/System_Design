from __future__ import annotations
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def send(self, mediator, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass

class Mediator:
    def __init__(self):
        self.users = []
    
    def add_user(self, user:RealUser):
        self.users.append(user)
    
    def notify_all(self, msg, sender):
        for user in self.users:
            if sender.name != user.name:
                user.receive(msg)

class RealUser(User):
    def __init__(self, name, mediator:Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def send(self, msg):
        print(f"\n{self.name} >> SENDING >> {msg}")
        self.mediator.notify_all(msg, self)
    
    def receive(self, msg):
        print(f"  {self.name} << RECEIVING << {msg}")
    
mediator = Mediator()
nick = RealUser("nick", mediator)
steeve = RealUser("steeve", mediator)
tony = RealUser("tony", mediator)
stark = RealUser("stark", mediator)

mediator.add_user(nick)
mediator.add_user(steeve)
mediator.add_user(tony)
mediator.add_user(stark)

nick.send("Nick Reporting")
steeve.send("steeve Reporting")
tony.send("tony Reporting")
