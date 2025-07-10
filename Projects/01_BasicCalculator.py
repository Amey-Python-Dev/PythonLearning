#=============================== Calculator ===============================================

print("Welcome to Basic Calculator, by Amey...")
num1 = float(input("Enter your First number: "))
num2 = float(input("Enter your Second number: "))

print("Choose operation: +, -, *, /")
print("For First number to the Power of Second number use: **")
print("If you use '%' then your numbers will be divided and remainder will be the output")
opt = input("Enter operator: ")

if (opt == "+"):
    print("Result:", num1 + num2)
elif (opt == "-"):
    print("Result:", num1 - num2)
elif (opt == "*"):
    print("Result:", num1 * num2)
elif (opt == "/"):
    if (num2 != 0):
        print("Result:", num1 / num2)
    else:
        print("Error: Division by Zero is undefined.")
elif (opt == "**"):
    print("Result:", num1 ** num2)
elif (opt == "%"):
    print("Result:", num1 % num2)
else:
    print("Invalid Operator!")
    print("Retry")
print("Congratulations Your calculation is done!!")