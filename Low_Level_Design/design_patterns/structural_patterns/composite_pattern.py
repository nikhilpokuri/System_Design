#---------------------------Example-01--------------------------------------
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, space=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name) -> None:
        self.name = name
    
    def display(self, space=0):
        print(" " * space + "|~" + self.name)

class Directory(FileSystemComponent):
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
    
    def add_component(self, component:FileSystemComponent):
        self.children.append(component)

    def display(self, space=0):
        print(" " * space + "|-" + self.name)
        for child in self.children:
            child.display(space + 2)

#client
root = Directory("root")

dir1 = Directory("dir1")
file1 = File("file-1-1")
file2 = File("file-1-2")
dir1.add_component(file1)
dir1.add_component(file2)

dir2 = Directory("dir2")
file3 = File("file-2-1")
file4 = File("file-2-2")
dir2.add_component(file3)
dir2.add_component(file4)

root.add_component(dir1)
root.add_component(dir2)

print("\tEXAMPLE_01_OUTPUT\n")
root.display()




#---------------------------Example-02 [General]--------------------------------------

class Equipment:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Composite:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, equipment:Equipment):
        self.items.append(equipment)
        return self
    
    def price(self):
        return sum([item.price for item in self.items])

#client
computer = Composite("PC")
keyboard = Equipment("Keyboard", 2000)
cpu = Equipment("CPU", 4000)
mouse = Equipment("Mouse", 500)
computer.add_item(keyboard).add_item(cpu).add_item(mouse)

memory = Composite("Memory")
ram = Equipment("RAM", 3000)
rom = Equipment("ROM", 2500)
memory.add_item(ram).add_item(rom)

print("\n\n\tEXAMPLE_02_OUTPUT\n")
print(f"Price of Computer with Equipment {[item.name for item in computer.items]}: {computer.price()}")
print(f"Price of Memory with Equipment {[item.name for item in memory.items]} {memory.price()}")