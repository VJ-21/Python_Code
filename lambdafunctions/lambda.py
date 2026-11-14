"""
In python lambda functions are anonymous functions without a name.It has lambda keyword and has the following syntax:
lambda arguments:expression

Lambda functions are often used in situations where a small function is required for a short period of time. 
They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
# Function to double the input

def double(x):
    return x * 2

# Lambda function to double the input
double = lambda x: x * 2
cube = lambda x:x*x*x
use on one liner rather than on the multiple lines you can pass lambda as argument to functions which is main usage 
you pass function to another function 
The above lambda function has the same functionality as the double function defined earlier. 
However, the lambda function is anonymous, as it does not have a name.

Lambda functions can have multiple arguments, just like regular functions. 
Here is an example of a lambda function with multiple arguments:
"""
double = lambda x: x * 2
cube = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/2

print(double(5))
print(cube(3))
print(avg(3,5,10))

#passing function as argument to another function
def appl(fx,value):
    return 6*fx(value)

print(appl(cube,2))
print(appl(lambda x:x*x,2))


