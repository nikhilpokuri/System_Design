from abc import ABC, abstractmethod

class Observer(ABC):
    """Abstract Observer"""

    @abstractmethod
    def set_temperature(self, temperature:int):
        pass

class WeatherStation:
    """Subject Class"""

    def __init__(self):
        self.__subsribers = []

    def subscribe(self, observer:Observer):
        self.__subsribers.append(observer)
    
    def unsubscribe(self, observer:Observer):
        self.__subsribers.remove(observer)

    def notify_all(self, temperature:int):
        for subcriber in self.__subsribers:
            subcriber.set_temperature(temperature)
            print()

class AirConditionerObserver(Observer):
    """Concrete AirConditioner Observer"""

    def set_temperature(self, temperature: int):
        if temperature > 25:
            print(f"  Current Tempareture: {temperature}\n(AC-CONTROLLER): Too Hot...Turning On Air Conditioner")
        else:
            print(f"  Current Tempareture: {temperature}\n(AC-CONTROLLER): It's Normal...Turning Off Air Conditioner")
    
class GeyserObserver(Observer):
    """Concrete Geyser Observer"""

    def set_temperature(self, temperature: int):
        if temperature > 25:
            print(f"  Current Tempareture: {temperature}\n(GEYSER-CONTROLLER): Too Hot...Turning On Geyser")
        else:
            print(f"  Current Tempareture: {temperature}\n(GEYSER-CONTROLLER): It's Normal...Turning Off Geyser")

station = WeatherStation()
ac = AirConditionerObserver()
heater = GeyserObserver()

station.subscribe(ac)
station.subscribe(heater)
station.subscribe(heater)
station.unsubscribe(heater)

station.notify_all(25)