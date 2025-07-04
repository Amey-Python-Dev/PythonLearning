print("Hello World")
print(5)
print(5 + 2) #same syntax is used for subtraction,multiplication, division ie. -, *, /
# for single-line comment use "#" for multiple-line comment use '''.....''' or """" ....  """"
print("hey my name is Amey Pawar \n I have started learning python.") # '\n' is to create a new line in text output. and it is called escape sequence

# An escape sequence character is a backslash '\' followed by the character you want to insert eg is given below
'''
print("Hello my name is "Amey", I am a boy")
this gives a error showing that syntax is invalid because of "Amey"
if we want to give "..." in a string then use escape sequence character
'''
print("Hello my name is \"Amey\", I am a boy ") # output => Hello my name is "Amey", I am a boy 
print("amey", 5, 6) #Python print can consist string & number at once.
print("Rider", 143, "riding") # here ' ' space is default separater we can change it, given as below
print("Rider", 143, "riding", sep="_", end=" the end") # when we have to end our print with something then use this syntax