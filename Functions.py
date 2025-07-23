'''
 Function declaring syntax:
 def function_name(parameter):
    -function body-
    return value

-------------------------------------
def function_name(parameter):
    pass
this is used when we know that we need this function but we will declare its body in future
 '''

#eg:
def greet(name):
    print("hello", name)

greet("amey") # output=> hello amey

'''
types of functions:-
> Built-in functions => in which print(), len(), type(), input() is used
> User defined functions => which we create using def
> Lambda Functions => Ek-line anonymous functions
'''

'''
Function Arguments and return statement
There are four types of arguments that we can provide in a function:
> Default Arguments
> Keyword Arguments
> Variable length Arguments
> Required Arguments
'''

# Default arguments example:
def average(a=1, b= 5): # Here a & b default value is fixed ie. 1 & 5 
    print("the average is:", (a+b)/2)

average(b= 7) # here default value of a is used and b value is new one

# Keyword Arguments: We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
# example:
average(b=9, a=3)

#Required Arguments:
def new_average(a, b=3): # here default value of a is not declared hence we are required to give the value of a when we call function
    print("the average is:", (a+b)/2)

new_average(a=3, b=5) # here if we don't assigned any value for b then default value will be used

# Variable length Arguments:
#Example1 (tuple):
def average2(*numbers):
    #print(type(numbers)) => tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))

average2(1, 5, 4, 10)

#Example2 (dictionary):
def name(**names):
     #print(type(names)) => dictionary
     print("Hello,", names["fname"], names["mname"], names["lname"])

name(mname = "Prakash", lname = "Pawar", fname = "Amey")

# Return statement: The return statement is used to return the value of the expression back to the calling function
# Eg:
def average3(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum / len(num)
c = average3(2, 3, 4, 1)
print(c)