# Hiding the implementation details of a class and only showing the essential features to the user.
# Below are few examples for creating the abstract classes for creating the abstract classes at least one abstract method should be defined in the class.
# To define we need to import the abc module and need to use that ABC,abstract decorator in the definition to make the class abstract class
from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.n=n
    @abstractmethod
    def start(self,color):
        pass


# Now above class became the abstract class and you cannot create object on that
