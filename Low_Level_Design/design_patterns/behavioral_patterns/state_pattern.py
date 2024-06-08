from __future__ import annotations

from abc import ABC, abstractmethod

class LightState(ABC):
    """Abstract Light State"""
    @abstractmethod
    def handle(self):
        pass

class RedLight(LightState):
    """Concrete RED Light State"""

    color = "red"

    def handle(self, traffic:Traffic):
        print("(CURRENT): Red..STOP")
        traffic.set_light(YellowLight())

class YellowLight(LightState):
    """Concrete YELLOW Light State"""

    color = "yellow"
    
    def handle(self, traffic:Traffic):
        print("(CURRENT): Yellow..WAIT")
        traffic.set_light(GreenLight())


class GreenLight(LightState):
    """Concrete GREEN Light State"""
    color = "green"
    
    def handle(self, traffic:Traffic):
        print("(CURRENT): Green..GO")
        traffic.set_light(RedLight())

class Traffic:
    prev = None
    light = RedLight()

    def set_light(self, light:LightState):
        self.light = light
    
    def red_light(self):
        if self.light.color == "red":
            self.prev = True
            return self.light.handle(self)
        else:
            print(f"(ERROR): Next should be {self.light.color}")

    def yellow_light(self):
        if self.prev == None:
            print("(ERROR): RED should be first")
            return
        if self.light.color == "yellow":
            return self.light.handle(self)
        else:
            print(f"(ERROR): Next should be {self.light.color}")

    def green_light(self):
        if self.prev == None:
            print("(ERROR): RED should be first")
            return
        if self.light.color == "green":
            return self.light.handle(self)
        else:
            print(f"(ERROR): Next should be {self.light.color}")


#client
"""
CORRECT STATES: red -> yellow -> green
"""
traffic = Traffic()

traffic.red_light()
traffic.yellow_light()
traffic.green_light()

traffic.yellow_light()