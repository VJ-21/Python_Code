class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())


# __acc_pass is a private variable (name mangled by Python).
""" If we want to make private class or method we need to add two underscore like above __acc_pass, only class internal
functions can access the private methods or attributes
for accessing the private method create one more normal  method and access the private method there and call that public method
with the object
"""
# The line print(acc1.reset_pass()) will:
# Print "abcde" (from inside the method).
# Then print None (because reset_pass() doesn't return anything).


