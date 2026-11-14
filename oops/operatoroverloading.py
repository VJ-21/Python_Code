class Complex_number:
    def __init__(self,real_num,img_num):
        self.real=real_num
        self.img=img_num


    def show_number(self):
        print(str(self.real)+"i+",str(self.img)+"j")


    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex_number(newReal,newImg)

    def __str__(self):
        return f"{self.real}i + {self.img}j" 

num1=Complex_number(1,2)
num1.show_number()

num2=Complex_number(3,4)
num2.show_number()

num3=num1+num2
num3.show_number()
#print(num3)

""" 🔧 What is __add__?

__add__ is a special method in Python, called a "dunder method" (short for “duble underscore”).

It tells Python how to handle the + operator when it's used with objects of a class you’ve defined."""