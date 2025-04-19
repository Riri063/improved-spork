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