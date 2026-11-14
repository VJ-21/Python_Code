
"""
Methods that dont use the self parameter (work at class level) not at object level means for objects we are using the self if
there is no need of objects then its class level.
static method converts a function to be static method no need for self

"""


class Student:
    @staticmethod  # decorator
    def College():
        print("ABC COllege")


s1 = Student()
s1.College()
# ?Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function
# ?without permanently modifying it.
