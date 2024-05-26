from abc import ABC, abstractmethod

class Device(ABC):
    volume = 0

    @abstractmethod
    def get_name(self):
        pass

class Radio(Device):
    def get_name(self):
        return "Device: Radio"

class Television(Device):
    def get_name(self):
        return "Device: Television"

class HomeTheater(Device):
    def get_name(self):
        return "Device: HomeTheater"

class Speaker(Device):
    def get_name(self):
        return "Device: Speaker"
    
class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class BasicRemote(Remote):
    def __init__(self, device:Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        return f"{self.device.get_name()} \nVolume: {self.device.volume}"
    
    def volume_down(self):
        self.device.volume -= 1
        return f"{self.device.get_name()} \n Volume: {self.device.volume}"

#client
radio_remote = BasicRemote(Radio())
television_remote = BasicRemote(Television())
homeTheater_remote = BasicRemote(HomeTheater())
speaker_remote = BasicRemote(Speaker())

radio_remote.volume_up()
radio_remote.volume_up()
radio_remote.volume_down()

television_remote.volume_up()
television_remote.volume_up()

homeTheater_remote.volume_up()
homeTheater_remote.volume_down()
homeTheater_remote.volume_up()

speaker_remote.volume_up()
speaker_remote.volume_down()

print("Radio:",radio_remote.device.volume)
print("Television:", television_remote.device.volume)
print("Home Theater:", homeTheater_remote.device.volume)
print("Speaker:", speaker_remote.device.volume)