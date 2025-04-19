# 2. Check Password Strength
# This function checks if the password is strong or weak.
def check_password_strength():
    password = input("Enter a password : ")

    # If the password is too short, it's weak
    if len(password) < 8:
        print("Weak password: Too short")
    # If the password is only letters or only numbers, it's weak
    elif password.isalpha() or password.isdigit():
        print("Weak password: Must contain letters and numbers")
    # Otherwise, it's a strong password
    else:
        print("Strong password")

# Example usage
check_password_strength()  # This will prompt the user for input
