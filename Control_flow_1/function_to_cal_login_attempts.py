def login_attempts(max_attempts):
    attempts = 0
    correct_password = "password123"  # Example password (in a real scenario, never store passwords in plain text!)
    
    while attempts < max_attempts:
        user_input = input("Enter your password: ")
        if user_input == correct_password:
            print("Login successful!")
            return True
        else:
            attempts += 1
            print(f"Incorrect password. Attempts left: {max_attempts - attempts}")

    print("Too many failed attempts. Access denied.")
    return False
login_attempts(10)
