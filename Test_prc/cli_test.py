# Command line utilities are programs that can be run from terminal or command line interface.
# They are essential part of many development workflows.
# In python you can create your own command line utilities using built in argparse module
# Two types of arguments we can parse positional arguments  and the optional arguments
# Whenever you pass argument through terminal or command prompt it comes back as string so we have to convert it accordingly 

import argparse


# if __name__=="__main__":
#     parser=argparse.ArgumentParser()
#     parser.add_argument("number1",help="This is the first number")
#     parser.add_argument("number2",help="This is the second number")
#     parser.add_argument("Operation",help="This is the operation which user want to perform")

#     args=parser.parse_args()

#     n1=int(args.number1)
#     n2=int(args.number2)
#     result=None
#     if args.Operation=="add":
#         result=n1+n2
#     elif args.Operation=="Subraction":
#         result=n1-n2

#     print("Result is :",result)

# Making positional arguments to the optional arguments by adding -- infront of postional arguments

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--number1",help="This is the first number")
    parser.add_argument("--number2",help="This is the second number")
    parser.add_argument("--Operation",help="This is the operation which user want to perform",choices=["add","Subraction"])

    args=parser.parse_args()

    n1=int(args.number1)
    n2=int(args.number2)
    result=None
    if args.Operation=="add":
        result=n1+n2
    elif args.Operation=="Subraction":
        result=n1-n2
    print("Result is :",result)


"""
ArgumentParser():Creates a parser object (class constructor)
add_argument():Adds argument definitions to the parser
parse_args():Parses command-line inputs and returns a Namespace object
One important distinction:
parser should convert the input into objects.
More precisely, parse_args() converts the command-line inputs into a Namespace object,where each argument is available as an attribute.
"""