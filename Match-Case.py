#====================================================== Match-Case ======================================================

'''
Syntax:-
match variable:
    case value1:
        # action1
    case value2:
        # action2
    case _:
        # default action (like else) 
'''

#----------------------------- With Numbers ----------------------------------

num = 2 # you can use input() to take number from user

match num:
    case 1: # no need to show 'num = 1'
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("other number")


#----------------------------- Multiple Values in one case -----------------------

fruit = "apple"

match fruit:
    case "apple" | "banana" | "mango": # '|' it means 'or'
        print("This is a fruit")
    case _:
        print("Not a fruit")


#------------------------ Pattern Matching with Tuples --------------------------

point = (1, 2)

match point:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f"Y axis at {y}")
    case (x, 0):
        print(f"X axis at {x}")
    case (x, y):
        print(f"point is at ({x}, {y})")


#------------------------ Match With Conditions (Guards) -----------------------------

age = 17

match age:
    case a if a < 18:
        print("Minor")
    case a:
        print("Major")

    
#----------------------------------  Real-Life Example -----------------------------------
#                                      (Login Option)

option = input("Choose option(login, signup, exit): ")

match option:
    case "login":
        print("Logging in...")
    case "signup":
        print("Creating account...")
    case "exit":
        print("Exiting app...")
    case _:
        print("Invalid option")