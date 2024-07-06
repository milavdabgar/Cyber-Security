def encrypt_rail_fence(plaintext, key):
    rail = [['\n' for i in range(len(plaintext))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    
    for char in plaintext:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1
    
    result = []
    for i in range(key):
        for j in range(len(rail[i])):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def decrypt_rail_fence(ciphertext, key):
    rail = [['\n' for i in range(len(ciphertext))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    
    for char in ciphertext:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1
    
    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    
    result = []
    row, col = 0, 0
    for char in ciphertext:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)

# Test the functions
plaintext = input("Enter plain text:")
key = 3
ciphertext = encrypt_rail_fence(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt_rail_fence(ciphertext, key)
print(f"Decrypted: {decrypted}")
