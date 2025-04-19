# 1. Greet User Function
# This function says hello to the user using their name.
def greet_user(name):
    # It prints a message with the user's name
    print(f"Hello, {name}! Welcome to the system.")

# Example usage
greet_user("Fatiha")  # This will print: "Hello, Fatiha! Welcome to the system."


# 2. Authenticate User Based on Username and Password
# This function checks if the username and password are correct.
users = {
    "admin": "secure123",
    "user1": "password456"
}

def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if the username and password match
    if username in users and users[username] == password:
        print("Access granted!")
    else:
        print("Invalid credentials.")

# Example usage
authenticate()  # This will prompt the user for input


# 3. Check Password Strength
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

#gdh Example usage
check_password_strength()  # This will prompt the user for input


# 4. Track Failed Login Attempts
# This function lets the user try logging in a few times and keeps track of failed attempts.
failed_logins = []

def login_attempts_with_tracking(max_attempts):
    # Correct password
    PWD = "secure123"
    # Start with 0 attempts
    attempts = 0
    
    # Keep asking for password until the user runs out of attempts
    while attempts < max_attempts:
        # Ask the user to type in their password
        password = input("Enter password: ")
        
        # If the password is correct, let them in
        if password == PWD:
            print("Access granted!")
            break
        else:
            # If the password is wrong, add 1 to attempts
            attempts += 1
            # Add "Failed Attempt" to the list
            failed_logins.append("Failed Attempt")
            # Tell them how many attempts they have left
            print(f"Incorrect password. Attempts left: {max_attempts - attempts}")
    
    # If they run out of attempts, lock them out and print failed attempts
    else:
        print("Account locked due to multiple failed attempts!")
        print(f"Failed login attempts: {len(failed_logins)}")

# Example usage
login_attempts_with_tracking(3)  # This will prompt the user for input


# 5. Check Suspicious IP Addresses
# This function checks if an IP address is in the blocked list.
blocked_ips = {"192.168.1.1", "10.0.0.5"}

def check_ip():
    ip = input("Enter an IP address to check: ")
    
    # If the IP is in the blocked list, show a warning
    if ip in blocked_ips:
        print("Suspicious activity detected!")
    else:
        print("IP is safe.")

# Example usage
check_ip()  # This will prompt the user for input
