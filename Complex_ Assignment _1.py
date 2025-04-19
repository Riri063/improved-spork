# Function to greet a user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the system.")  # Print a greeting message with the user's name

# Function to check if password is weak
def check_password_strength(password):
    if len(password) < 8:  # Check if the password length is less than 8 characters
        print("Weak password: Too short")  # Print message if password is too short
    elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):  # Check if the password contains both letters and digits
        print("Weak password: Must contain both letters and numbers")  # Print message if password doesn't meet criteria
    else:
        print("Strong password")  # Print message if the password is strong

# Function to handle username input
def input_username():
    return input("Enter username: ")  # Prompt the user to enter a username and return the value

# Function to handle password input
def input_password():
    return input("Enter password: ")  # Prompt the user to enter a password and return the value

# Function to check if credentials are correct
def check_credentials(username, password):
    if authenticate(username, password):  # Call the authenticate function to check if username and password are correct
        print("Access granted!")  # Print success message if credentials are correct
        return True  # Return True if login is successful
    else:
        print("Invalid credentials.")  # Print error message if credentials are incorrect
        return False  # Return False if login fails

# Function to handle login attempts
def login_attempts(max_attempts):
    attempts = max_attempts  # Set the maximum number of attempts
    failed_logins = []  # Initialize an empty list to track failed login attempts

    while attempts > 0:  # Loop while there are attempts remaining
        username = input_username()  # Get the username input
        password = input_password()  # Get the password input
        if check_credentials(username, password):  # Check if the provided credentials are correct
            return  # Exit the function if login is successful
        else:
            attempts -= 1  # Decrease the number of remaining attempts
            failed_logins.append("Failed Attempt")  # Add a failed attempt entry to the list
            if attempts == 0:  # If no attempts are left
                print("Account locked due to multiple failed attempts!")  # Notify the user that the account is locked
                print(failed_logins)  # Print the list of failed login attempts
            else:
                print(f"Incorrect password. Attempts left: {attempts}")  # Show how many attempts are left

# Function to authenticate username and password
def authenticate(username, password):
    if username in users and users[username] == password:  # Check if the username exists and the password matches
        return True  # Return True if authentication is successful
    return False  # Return False if authentication fails

# Function to handle IP checking
def check_ip(ip):
    if ip in blocked_ips:  # Check if the IP is in the list of blocked IPs
        print("Suspicious activity detected!")  # Print message if the IP is blocked
    else:
        print("IP is safe.")  # Print message if the IP is not blocked

# Dictionary to store users and passwords
users = {
    "admin": "secure123",  # Username 'admin' with password 'secure123'
    "user1": "password123"  # Username 'user1' with password 'password123'
}

# Set to store blocked IP addresses
blocked_ips = {"192.168.1.1", "10.0.0.5"}  # Set containing blocked IPs

# Main flow function
def main():
    greet_user("Fatiha")  # Call the greet_user function to print a greeting message
    check_password_strength("Pass123")  # Call the check_password_strength function to evaluate the password strength
    login_attempts(3)  # Call the login_attempts function with a maximum of 3 login attempts
    check_ip("192.168.1.1")  # Call the check_ip function to check if the IP is blocked

# Run the main function
main()  # Call the main function to execute the programt