"""The super() keyword in Python is used to refer to the parent class. 
It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
However, sometimes you might want to use the parent class method in the child class. 
This is where the super() keyword comes in handy."""

#        Car (Parent)
#         ↑
#    ToyotaCar (Child)
#         ↑
#    Fortuner (Grandchild)
# super() helps us go one level up ⬆ and reuse what is already defined.
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)     # Call the parent constructor
        self.roll_no = roll_no

s1 = Student("Ravi", 101)
print(s1.name)      # Ravi (from parent)
print(s1.roll_no)   # 101 (from child)
