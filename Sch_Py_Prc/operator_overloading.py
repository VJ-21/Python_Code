#operators are +,-,*

class sum_operation:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        self.other=other
        return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
    

c1=sum_operation(1,2)
c2=sum_operation(3,4)

print(c1+c2)


