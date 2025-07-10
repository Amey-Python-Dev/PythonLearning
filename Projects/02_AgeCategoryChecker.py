print("Welcome! to the Age Category Checker")
age = float(input("Enter your age: "))

if (age <= 0):
    print("Error: You have entered the wrong age")
elif (0 < age < 13):
    print("You are from Child Category.")
elif (13 <= age < 20 ):
    print("You are from Teenager Category.")
elif (20 <= age < 60):
    print("You are from an Adult Category.")
else:
    print("You are from Senior Citizen Category.")
print("Congratulations! This was your Age Category.")