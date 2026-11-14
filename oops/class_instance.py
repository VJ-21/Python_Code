"""Class attributes will be same for all objects in the class like college name remains same in DB.
But instance attributes will be different for all  objects like name. 
we will define them by self.attribute_name like name,marks
Attribute means the data or variable like name,marks etc
Object attribute name="VK" is greater than class attribute  name= "VN" , vk will get printed""" 


class Student:
    #college_name is common so we made it as class attribute and store it once
    # we did not defined college_name with self it stores in memory once self is for storing 
    # multiple instance .
    college_name="Jain University"
    def __init__(self,fullname,std_marks):
        self.name=fullname
        self.marks=std_marks
        print("Adding new student in database..")
#init function invokes automatically  at object creation
#creating the object
s1=Student("Ram Krishna","89")
print(s1.name,s1.marks)
print(Student.college_name)