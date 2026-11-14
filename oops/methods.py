"""
class contains the attributes(data) or properties and methods
Methods are functions that belong to objects
"""
class Student:
    college_name="Jain University"
    def __init__(self,fullname,std_marks):
        self.name=fullname
        self.marks=std_marks
        print("Adding new student in database..")
    
    def welcome(self):
        print("Welcome student,",self.name)

    def get_marks(self):
        print("Final Marks,",self.marks)

s1=Student("Virat","89")
print(s1.name,s1.marks)
s1.welcome()
s1.get_marks()