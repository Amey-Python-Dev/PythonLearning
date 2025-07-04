# this is the syntax for declaring any variable in python
a = 12838 # number datatype
b = "Amey" # string Datatype
c = True # boolean datatype
d = None # none  datatype
e = 1.3
f = complex(8, 9) #syntax to declare 'complex(realNumber, imaginaryNumber) or else just just declare realNum +/- imaginaryNumj as given below
g = 8 + 2j

print(a) # for printing the value stored in that variable

# Method to check the datatype 
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'bool'>
print(type(d)) # <class 'NoneType'>
print(type(e)) # <class 'float'>
print(type(f)) # <class 'complex'> same for type(g)

# LIST & TUPLE
list1 = [1, 2.3, [-4, 5], "amey", 'rider', 8+6j] # this is list datatype in which we can contain all types of datatype in collection form
print(list1)
print(type(list1)) # <class 'list'>

tuple1 = ("arrow", "sparrow", (3.4, 4), 3, 3+2j) # this is tuple datatype in which we can contain all type of datatype in collection form
print(tuple1)
print(type(tuple1)) # <class 'tuple'>

# Difference between tuple and list: the collection in list can be modified that means we can change it but we cannot modify collection stored in tuple

'''
Mapped Data: dict
dict: A dictionary is an unordered collection of data containing a key:valuePair
      The key:valuePairs are enclosed within curly brackets
      Note: here the key should be defined as sam
'''
dict1 = {
    "name": "Sam",
    "Age": 18,
    "canvote": True
    }
print(dict1)
print(type(dict1)) # <class 'dict'>



#----------------------------------------- Some Basics of Math----------------------------------------------------

print(15*6) # multiplication ie. 15x6
print(15**6) # exponential that means 15^6
print(15/6) # division
print(15//6) # Floor division ie. after division the closest small integer will be output
print(15%9) # Modulus ie. remainder will be output

#--------------------------------- Tasks form chatgpt---------------------------------------------
#TASK 1
name = "Amey"
age = 18
grade = "12th"

print(f"My name is {name}. I am {age} years old and studing in {grade} grade.") # f" " : formatted string, it replaces variable written in {} into its actual value

#TASK 2
#Method1
x = 5
y = 10

a = x  # step1: consider a new variable equals to first variable
x = y  # step2: equate x = y
y = a  # step3: equate second variable with new variable

print("x=", x)
print("y=", y)
#Method2
b = 1
c = 2

b, c = c, b

print("b=", b)
print("c=", c)
