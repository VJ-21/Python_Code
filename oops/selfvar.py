class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new student in database..")
#init function invokes automatically  at object creation
#creating the object
s1=Student("rat")
print(s1.name)
# here s1 and s2 are object names but internally they are self
s2=Student("mouse")
print(s2.name)
# The self parameter is a reference to the current instance of the class
# It  is used to access variables belongs to the class
