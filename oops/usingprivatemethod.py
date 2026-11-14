class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())

# What it does:
# __hello() is a private method, only accessible inside the class.
# welcome() is a public method that calls the private __hello() method.
# p1.welcome() prints "hello person!" from inside the method.
# Then print(p1.welcome()) prints None because welcome() doesn’t return anything — it just prints.


# 🔒 Private(like) attributes & methods in Python
# ✅ Conceptual Implementations in Python:

#? Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.


"""str = “I am a coder.”

str.endswith(“er.”)     #returns true if string ends with substr

str.capitalize( )       #capitalizes 1st char

str.replace( old, new ) #replaces all occurrences of old

str.find( word )        #returns 1st index of 1st occurrer

str.count(“am”)         #counts the occurrence of substr """


"""
🔷 What is a Class?

A class is like a blueprint for creating objects.
It defines attributes (data) and methods (functions) that the objects created from the class will have.

🔷 What is an Object?

An object is an instance of a class.
It contains actual values stored in memory and can use the methods defined in the class."""