from abc import ABC, abstractmethod
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class HighResolutionImage(Image):
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_image()
    
    def load_image(self):
        print(f"High Resolution Image Loading: {self.file_path}")
        
    def display(self):
        print(f"Displaying High Resolution Image: {self.file_path}")

class ProxyImage(Image):
    def __init__(self, file_path):
        self.file_path = file_path
        self.real_img_status = None

    def display(self):
        if self.real_img_status == None:
            print(f"Displaying Proxy Image: {self.file_path}")
            self.real_img_status = HighResolutionImage(self.file_path) 
        else:
            self.real_img_status.display()

#Client
img1 = ProxyImage("pics/nick.jpg")
img2 = ProxyImage("pics/steeve.jpg")

"""ProxyImage will display first and then load the actual image on demand"""
img1.display() # ProxyImage is shown first, then loads the high-resolution image
img1.display() # Now displays the high-resolution image

print()

img2.display() # ProxyImage is shown first, then loads the high-resolution image
img2.display() # Now displays the high-resolution image

