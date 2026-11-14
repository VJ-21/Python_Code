class Student:
    #default constructors
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self,fullname,student_mark):
        self.name=fullname
        self.marks=student_mark
        print("Adding new student in database..")

s1=Student("rat","100")
print(s1.name,s1.marks)
