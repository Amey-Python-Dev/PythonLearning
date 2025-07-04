'''
->TypeCasting: when a datatype is changed to another datatype it is called typecasting. They are of 2 types implicit and explicit.
->Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dic(), etc for type casting in python
=> Implicit type casting: According to the order of datatype, one datatype is converted into other by the Python interpreter itself  
=> Explicit type casting: The conversion of one datatype into another datatype is done manually 
'''

# Explicit Example:
string = "4"
number = 3
string_number = int(string) # here string is converted into number
sum = string_number + number 
print(sum) # output=> 7

# Implicit Example:
a = 1.678
b = 2
print(a + b) # output=> 3.678 ,   here int is converted into float datatype automatically and then operation is performed.