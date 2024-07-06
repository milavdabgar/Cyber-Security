import random

def generate_large_prime():
    """Generate a large prime number."""
    while True:
        #num = random.randint(10**9, 10**10)  # Generate a random 10-digit number
        num = random.randint(10**0+3, 100)  # Generate a random number
        if is_prime(num):
            
            return num

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(a, m):
    """Calculate the modular multiplicative inverse."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    """Generate a RSA key pair."""
    p = generate_large_prime()
    q = generate_large_prime()
    print("first prime no:",p)
    print("second prime no:",q)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = modular_inverse(e, phi)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    """Encrypt a message using a public key."""
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    """Decrypt a message using a private key."""
    n, d = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Test the encryption and decryption
message = input("Enter plain text:")
public_key, private_key = generate_keypair()
print("public key:",public_key)
print("private key:",private_key)
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
