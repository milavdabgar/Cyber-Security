def encrypt_caesar(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

# Test the functions
plaintext = input("Enter plain text:")

shift = int(input("Enter integer number:"))
ciphertext = encrypt_caesar(plaintext, shift)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt_caesar(ciphertext, shift)
print(f"Decrypted: {decrypted}")
