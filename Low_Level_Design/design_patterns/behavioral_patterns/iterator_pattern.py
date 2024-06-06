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
    def __init__(self, collection, reverse=False) -> None:
        self.__collection = collection
        self.reverse = reverse
        self.index = -1 if reverse else 0
    
    def has_next(self):
        return -len(self.__collection) <= self.index < len(self.__collection)
    
    def next(self):
        if self.has_next():
            value = self.__collection[self.index]
            self.index += -1 if self.reverse else 1
            return value
        raise StopIteration("Cannot Iter Beyond Limit")
        

class NumberCollection(Aggregate):
    def __init__(self):
        self.__collection = []
    
    def add_element(self, element):
        self.__collection.append(element)
    
    def reverse_collection(self):
        return ListIterator(self.__collection, True)

    def create_iterator(self):
        return ListIterator(self.__collection)


#client
collection = NumberCollection()
collection.add_element(10)
collection.add_element(20)
collection.add_element(30)
collection.add_element(40)

iterator = collection.create_iterator() #normal traversal
iterator = collection.reverse_collection() #reverse traversal
# print(iterator.next())
while iterator.has_next():
    print(iterator.next())

# print(iterator.next()) #accessing more than the limit will raise exception