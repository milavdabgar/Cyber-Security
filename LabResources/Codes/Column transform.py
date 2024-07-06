def encrypt_columnar_transposition(plaintext, key):
    # Determine the number of columns
    col = len(key)
    # Determine the number of rows
    row = len(plaintext) // col + (len(plaintext) % col > 0)
    # Fill in the grid with plaintext characters row-wise
    matrix = [' ' for _ in range(row * col)]
    #print(matrix)
    for i in range(len(plaintext)):
        matrix[i] = plaintext[i]
    print(matrix)
    
    # Sort the key to determine the order of reading columns
    key_sequence = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''
    #print(key_sequence)
    
    # Read the matrix column-wise according to the sorted key
    for i in key_sequence:
        for j in range(row):
            #if matrix[j * col + i] != '':
                ciphertext += matrix[j * col + i]
    
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    # Determine the number of columns
    col = len(key)
    # Determine the number of rows
    row = len(ciphertext) // col
    if len(ciphertext) % col:
        row += 1
    # Create an empty matrix to fill in the characters column-wise
    matrix = ['' for _ in range(row * col)]
    
    # Sort the key to determine the order of filling columns
    key_sequence = sorted(range(len(key)), key=lambda k: key[k])
    
    index = 0
    # Fill the matrix column-wise according to the sorted key
    for i in key_sequence:
        for j in range(row):
            # Ensure we do not go out of bounds
            if index < len(ciphertext):
                matrix[j * col + i] = ciphertext[index]
                index += 1
    
    # Read the matrix row-wise to get the plaintext
    plaintext = ''
    for i in range(row):
        for j in range(col):
            if matrix[i * col + j] != '':
                plaintext += matrix[i * col + j]
    
    return plaintext

# Test the functions
plaintext = input("Enter plain text:")
key = input("Enter Key:")
ciphertext = encrypt_columnar_transposition(plaintext, key)
print("Encrypted text:",ciphertext)

key=input("Enter Key to decrypt:")

decrypted = decrypt_columnar_transposition(ciphertext, key)
print("Decrypted text:",decrypted)
