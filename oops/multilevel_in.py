class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)      # Call parent constructor
        self.type = type


car1 = Fortuner("Toyota", "diesel")
car1.start()
"""🧠 Summary:
Fortuner → ToyotaCar → Car (3-level inheritance).
Always use super().__init__() to call the parent constructor if you're overriding it.
Static methods like start() don't need self."""
