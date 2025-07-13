#================================ For Loops =======================================

'''
Syntax:
for variable in iterable: 
    # loop body (ye baar-baar chalega)

iterable meaning: List, string, range, etc — jiske elements pe loop chalega
variable meaning: 	Har step pe ye new value lega
for meaning: start of loop
in meaning: yeh keyword iterable ke through loop chalata hai
'''

#------------------ Loop in list -------------------------------

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(f"I like {fruit}")


#------------------- range() function ----------------------------

# syntax: range(start, stop, step)
# start => inclusive, default is 0
# stop => exclusive
# step => Kitne step mein badhna hai (default: 1)... consider step number = n so jo number first print hua hai uske baad jo number print hone wala hai un dono mein kitne numbers honge is n-1

# Example 1: 1 se 5 tak numbers print karo
for i in range(1, 6):
    print(i)

# Example 2: 0 se 10 tak ke even numbers (step=2)
for i in range(0, 11, 2):
    print(i)

# Example 3: Reverse loop (10 se 1 tak)
for i in range(10, 0, -1):
    print(i)
    

#---------------------- if-else in loops -----------------------------

for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


#-------------------- Extra  useful concepts -----------------------

for i in range(1, 10):
    if i == 5:
        print("Found 5, breaking the loop")
        break
    print(i)
# jab python 1 se 10 tak ke numbers ko print kr raha tha tab usko 5 dikhte he usne aage ke numbers print krna band kr diye


for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# idhar python ne pura range ko print kiya hai bss 3 number print nhi kiya and uske aage badh gaya because continue use kiya tha



#============================================= While Loop ===================================================================

'''
Syntax: 
while condition:
    # loop body
'''

# Example 1: Print 1 to 5 using while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1


#------------------ If-else in While loop ----------------

count = int(input("Enter current time (in seconds) shown on the bomb: "))

while count >= 0:
    if count == 0:
        print("Blast!")
    else:
        print(f"{count} seconds left")
    count -= 1


#--------------------- Infinite while loop -------------------

while True:
    command = input("Enter command (type 'exit' to quit): ")
    if command == "exit":
        print("Exiting loop.")
        break
    print(f"You typed: {command}")

# Ye loop tab tak chalta hai jab tak user "exit" nahi likhta.
