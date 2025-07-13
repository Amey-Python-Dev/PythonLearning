#===================== ATM Pin project ======================

real_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter your ATM pin: ")
    if pin == real_pin:
        print(f"Access Granted after {attempts} attempts.")
    else:
        print("Wrong Pin.")
        attempts += 1

if attempts == 3:
    print("Card blocked. Too many attempts.")