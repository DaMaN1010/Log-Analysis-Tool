# Import the necessary libraries
import re  # 're' provides regular expression operations for pattern matching
from collections import defaultdict  # Used to store counts of failed attempts per IP

# Define a function to parse the authentication log file
def parse_auth_log(filepath):
    # Create a dictionary where each IP will map to the number of failed login attempts.
    # defaultdict(int) automatically sets default value to 0 if a new key is accessed.
    failed_attempts = defaultdict(int)

    # Open the log file in read mode
    with open(filepath, 'r') as file:
        # Read the file line by line
        for line in file:
            # Only process lines that contain "Failed password"
            if "Failed password" in line:
                # Use regex to extract the IP address from the line.
                # Example line: "Failed password for root from 192.168.1.101 port 22"
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                
                # If an IP address is found
                if ip_match:
                    # Extract the IP address string (e.g., '192.168.1.101')
                    ip = ip_match.group(1)

                    # Increase the count of failed attempts for this IP
                    failed_attempts[ip] += 1

    # Print the results in a readable format
    print("\n--- Failed Login Attempts ---")
    for ip, count in failed_attempts.items():
        print(f"{ip}: {count} attempts")

# ----------- Main Program -----------
if __name__ == "__main__":
    log_path = input("Enter path to auth log file: ")  # e.g., /var/log/auth.log
    parse_auth_log(log_path)

