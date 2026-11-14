"""
Property decorator
The @property decorator in Python is used to define methods that behave like attributes — specifically, 
it allows you to access a method as if it were a regular variable, without needing parentheses ().

📦 What does @property really do?

It wraps a method in such a way that it can be accessed like an attribute, but still runs code behind the scenes.
below is the simple example for with or with out@ property method

"""
class Student:
      def __init__(self,sub_one,sub_two,sub_three):
            self.subject_one=sub_one
            self.subject_two=sub_two
            self.subject_three=sub_three
      
      @property
      def cal_percentage(self):
            return str((self.subject_one+self.subject_two+self.subject_three)/3)+"%"


s1=Student(99,90,89)

print(s1.cal_percentage)

s1.subject_three=99

print(s1.cal_percentage)

