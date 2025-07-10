# Conditional Operators: >, <, <=, >=, ==, !=
# type of output of input function is always string

# If-Else statements: In this we use only two conditions.
a = int(input("Enter your age:")) # int function is used to change string datatype output into integer
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
print("outside the conditional statement") # this output will not work according to the condition because it is not a part of condition
# The space used in conditional statement is called indentation


'''
 If-Elif-Else statements: 
 In this first we give If statement if it becomes true then python will not check further statements, and vise-versa.
 now Elif statements will be checked. In elif, we can put as much as conditions we want.
if all this conditions from above is not true then it will check else statement and will give output.
 '''
num = int(input("Enter your age: ")) # int(input()) throws an error if we use decimal value so we can use float, so we can give decimal value or integers.
if (0 < num <= 1):
    print("You are Infant.")
elif (1 < num <= 3):
    print("You are a Toddler.")
elif (3 < num <= 12):
    print("You are a Child.")
elif (12 < num <= 19):
    print("You are a Teenager.")
elif (19 < num <= 29):
    print("You are a Young Adult.")
elif (29 < num <= 39):
    print("You are an Adult.")
elif (39 < num <= 59):
    print("You are a Middle-aged.")
else:
    print("You are an Senior Citizen.")


#----------------- Nested If Statements -------------------
# It is just a code in which inside elif contains many conditions ie. elif ke andar if,elif,else.
x = 18
if (x < 0):
    print("Number is negative.")
elif (x > 0):
    if (x <= 10):
        print("Number is between 1-10")
    elif (x > 10 and x <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")