class Student:
    def __init__(self,age):
        self.__age=age
    def details(self,rank,roll_no,age):
        self.rank=rank
        self.roll_no=roll_no
        self.__age=age
    @property
    def rt_age(self):
        return self.__age
    @rt_age.setter
    def rt_age(self,new_age):
        self.__age=new_age+12

s1=Student(12)
print(s1.rt_age)
s1.rt_age=25
print(s1.rt_age)


 