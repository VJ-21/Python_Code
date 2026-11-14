class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.start())

"""
✅ Explanation:
Car is the base class with a color attribute and two static methods: start() and stop().
ToyotaCar is a child class that inherits from Car.
The start() method is marked with @staticmethod, so it can be called from the class or an instance without needing self.
car1.start() calls the start() method defined in the Car class.
"""