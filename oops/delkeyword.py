class Student:
    def __init__(self,name):
        self.name=name

s1=Student("shraddha")
del s1
print(s1)

# It will throw error saying you are deleting the object and you are trying to print it