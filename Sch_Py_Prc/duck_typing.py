class Animal:
    def speak(self):
        print("Animals can have different languague according to the species")
class Dog:
    def speak(self):
        print("Dog cannot speak but dog barks")
class car:
    def horn(self):
        print("Car cannot speak but they can horn")
class person:
    def speak(self):
        print("Humans can speak") 


def speak(obj):
    obj.speak()

a1=Animal()
d1=Dog()
c1=car()

speak(d1)

