# Strings are immutable ie. after deploying methods origin string will remain same
# space " " is also given a index in string
name = "Amey"
print("Hello,", name)

#---------------- Different types of strings methods to declare --------------------------------

#Type1: Double quotes("") inside string
a = "He said, \"I want to eat an apple\"" # here back slash'\'  is important because we enclosed a string in double quotes
print(a)
b = 'He said, "I want to eat an apple"'# here we have enclosed a string in quotes, so we can add double quotes inside the string.
print(b)

#Type2: Multiple line string
st = '''Hello Amey,
My name is python.
I am a \"computing language\". I was created in 1991.
I love that you are trying to learn me.'''
print(st) # here if you want a word to get enclosed in " " then use back slash.

#Type3: Getting an element of a particular index

print(name[0])
print(name[1])
print(name[2])
print(name[3])
# or else use as below
for character in name:
    print(character) # This is called Looping through the string    

#---------------------------------------------------------------------------------------

a = "AmeyPawar"
print(len(a)) #output => 9
print(a[0:4]) # syntax: string[x:y], x = from where we want to start(including first element)... b = where we want to end(exclusive last element)
print(a[0:-10]) 
print(a[::2]) #  Skip every 2nd character
print(a[-1:-3]) # here -1 mtlb 8th character hai, -3 mtlb 6th character hai (ie. 9-3)... so, [-1:-3]=~[8:6] since start>end => no output

#==============================================================================================

c = "Amey!!!"
print(c.upper()) # AMEY!!!
'''
same but different method
d = c.upper()
print(d)
'''
print(c.lower()) # amey!!!
print(c.rstrip("!")) # Amey


d = "Hi Amey, my name is amey, Amey is eating."
print(d.replace("Amey", "Sam")) # Hi Sam, my name is amey, Sam is eating.

print(d.count("Amey")) # it will count how much time the word is repeated in the string

print(d.find("is")) # Searches for the first occurrence of the given value and returns the index where it is present. If given value is absent then return -1.
print(d.index("is")) # same as is but it will throw an error if value is absent in string


e = "amey...!!!>>...rider"
print(e.split("...")) # ['amey', '!!!>>', 'rider'] here "e" string is separated by finding "..." And a new list is formed


blogHeading = "introduction TO jS" # this is going to be heading so only first letter should be capitalized and others shouldn't
print(blogHeading.capitalize()) # Introduction to js... the first character have upper case and the rest lower case

print(blogHeading.center(50)) # here with the help of center we are moving string to center part by just adding spaces in the beginning


f = "Welcome to the Console !!!"
print(f.endswith("!")) #True
print(f.endswith("!!")) #True
print(f.endswith("!!!")) #True
print(f.endswith("to", 2, 10)) # true ayega because 10th index pr to khatam ho raha hai, 0 iss liye dala to start from 1,2,3,..8 because fir to word start ho jayega
print(f.startswith("Welcome")) #True

g = "Welcome,Amey1"
h = "WelcomeAmey"
# isalnum() returns false if any other characters than (A-Z, a-z, 0-9) and when there is punctuations present
print(g.isalnum()) # false
print(h.isalnum()) # true
# isalpha is same just characters doesn't consist numbers
print(g.isalpha()) # false

print(h.islower()) # true if all characters in string are lower case, else it returns false
print(h.isupper()) ## true if all characters in string are capitalized, else it returns false

str1 = "We wish you Happy Birthday"
print(str1.isprintable()) # Return True if all characters in the string are printable, False otherwise.
print(str1.title()) # Return a version of the string where each word is titlecased.
print(str1.istitle()) # returns true only if the first letter of each word of the string is capitalized

str2 = "    "
print(str2.isspace()) # returns true if only string is made up of space

str3 = "Python is a Interpreted Language"
print(str3.swapcase()) #pYTHON IS A iNTERPRETED lANGUAGE


