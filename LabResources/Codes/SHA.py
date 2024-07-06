import hashlib

def sha1_hash(message):
    # Create a SHA-256 hash object
    sha1_hasher = hashlib.sha1()

    # Update the hash object with the message
    sha1_hasher.update(message.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    hex_digest = sha1_hasher.hexdigest()

    return hex_digest

# Prompt the user to enter a message
message = input("Enter message: ")

# Calculate the SHA-256 hash of the entered message
sha1_digest = sha1_hash(message)
print("SHA-1 hash of the entered message:", sha1_digest)

# Prompt the user to enter a message for comparison
message_again = input("Enter message again: ")

# Calculate the SHA-256 hash of the entered message
sha1_digest_again = sha1_hash(message_again)
print("SHA-1 hash of the entered message again:", sha1_digest_again)

# Compare the calculated hash with the provided hash
if sha1_digest == sha1_digest_again:
    print("Hashes match: Message has not been altered.")
else:
    print("Hashes do not match: Message may have been altered.")
