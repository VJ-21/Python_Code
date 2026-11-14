# class Person:
#     name="anonymous"

#     def changeName(self,name):
#         self.name=name

# p1=Person()
# p1.changeName("Raul kumar")
# print(p1.name)

# Instead of changing the name in class instance anonymous to raul kumar
# It is creating new attribute for the object

""" so another method is as below """
class Person:
    name="anonymous"

    def changeName(self,name):
        # Person.name=name #both the class and object instance changes to raul kumar,these and below are same
        self.__class__.name="Rahul"# Jiss bhi object ki class ko access karke value assign karna ho tho

p1=Person()
p1.changeName("rahul")
print(p1.name)


