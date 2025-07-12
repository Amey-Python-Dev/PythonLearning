#============================================ Password Strength Checker ===========================================================

Password = input("Enter your Password here: ")

# Length check
if not len(Password) > 8:
    print("❌ Password too short. Minimum 8 characters required.")

# Uppercase character check
if not any(char.isupper() for char in Password):
    print("❌ Add atleast one Uppercase letter.")

# Digit Check
if not any(char.isdigit() for char in Password):
    print("❌ Add atleast one Digit.")

# Special Character Check
if not any(not char.isalnum() for char in Password):
    print("❌ Add at least one special character.")
    
print("✅ Password check complete.")