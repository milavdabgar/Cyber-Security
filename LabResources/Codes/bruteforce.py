import time
import random
from datetime import datetime

# Brute force password cracking function
def crack_password(target_password):
    start_time = time.time()
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Simulate brute-force attack
    # For simplicity, let's assume the password consists of only lowercase letters and digits
    for char in target_password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit=True     
        if has_lower and has_upper and not has_digit:
            k=2
        elif has_lower and has_upper and has_digit:
            k=3
        elif has_lower and not has_upper and not has_digit:
            k=1
        elif not has_lower and has_upper and not has_digit:
            k=2
        elif not has_lower and not has_upper and has_digit:
            k=3
        elif has_lower and not has_upper and has_digit:
            k=3
        elif not has_lower and has_upper and has_digit:
            k=3
             
    print("value of k=",k)           
    if k==1:
        characters = 'abcdefghijklmnopqrstuvwxyz'
        print("Weak Password")
    elif k==2:
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print("Moderate Password")
    elif k==3:
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        print("Strong Password")
    password_length = len(target_password)
    attempts = 0

    # Loop through all possible password combinations until the target password is found
    found = False
    current_time = datetime.now()

    # Format the current time
    formatted_time = current_time.strftime("%H:%M:%S")

    print("Starting time:",formatted_time)
    while not found:
        password = ''.join(random.choice(characters) for _ in range(password_length))
        attempts += 1
        #print(password)
        if password == target_password:
            print("Password is:",password)
            current_time = datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S")
            print("Password crack at time:",formatted_time)
            found = True

    end_time = time.time()
    elapsed_time = end_time - start_time

    return attempts, elapsed_time


# Define passwords with different strengths


weak_password = input("Enter password using lowercase alphabet only:")

moderate_password = input("Enter password using uppercase and lowercase  alphabet:")

strong_password = input("Enter password using uppercase, lowercase  alphabet and digits:")



attempts, elapsed_time = crack_password(weak_password)
print(f"Time to crack weak password: {elapsed_time:.2f} seconds, Attempts: {attempts}\n")

attempts, elapsed_time = crack_password(moderate_password)
print(f"Time to crack moderate password: {elapsed_time:.2f} seconds, Attempts: {attempts}\n")

attempts, elapsed_time = crack_password(strong_password)
print(f"Time to crack strong password: {elapsed_time:.2f} seconds, Attempts: {attempts}\n")
