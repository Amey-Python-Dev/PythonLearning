#=============================== Calculator ===============================================

print("Welcome to Basic Calculator, by Amey...")

try:
    num1 = float(input("Enter your First number: "))
    num2 = float(input("Enter your Second number: "))

    print("Choose operation: +, -, *, /, **, %")
    opt = input("Enter operator: ")

    if opt == "+":
        print("Result:", num1 + num2)
    elif opt == "-":
        print("Result:", num1 - num2)
    elif opt == "*":
        print("Result:", num1 * num2)
    elif opt == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by Zero is undefined.")
    elif opt == "**":
        print("Result:", num1 ** num2)
    elif opt == "%":
        print("Result:", num1 % num2)
    else:
        print("Invalid Operator! Retry")

    print("Congratulations! Your calculation is done!!")

except ValueError:
    print("Error: You have entered non-numeric input (like A-Z or special characters). Please try again.")
