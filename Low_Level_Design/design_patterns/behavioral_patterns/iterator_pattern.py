from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class Aggregate(ABC):
    @abstractmethod
    def add_element(self, element):
        pass

    @abstractmethod
    def create_iterator(self):
        pass

class ListIterator(Iterator):
    def __init__(self, collection) -> None:
        self.__collection = collection
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.__collection)
    
    def next(self):
        if not self.has_next():
            raise StopIteration("Cannot Iter More Than Limit")
        self.index += 1
        return self.__collection[self.index - 1]

class NumberCollection(Aggregate):
    def __init__(self):
        self.__collection = []
    
    def add_element(self, element):
        self.__collection.append(element)
    
    def create_iterator(self):
        return ListIterator(self.__collection)


#client
collection = NumberCollection()
collection.add_element(10)
collection.add_element(20)
collection.add_element(30)
collection.add_element(40)

iterator = collection.create_iterator()
while iterator.has_next():
    print(iterator.next())

# print(iterator.next()) #accessing more than the limit will raise exception