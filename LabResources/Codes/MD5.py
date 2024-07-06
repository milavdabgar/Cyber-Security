import hashlib

def md5_hash(message):
    # Create an MD5 hash object
    md5_hasher = hashlib.md5()

    # Update the hash object with the message
    md5_hasher.update(message.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    hex_digest = md5_hasher.hexdigest()

    return hex_digest

# Prompt the user to enter a message
message = input("Enter message: ")

# Calculate the MD5 hash of the entered message
md5_digest = md5_hash(message)
print("MD5 hash of the entered message:", md5_digest)

# Prompt the user to enter a hash for comparison

message_again = input("Enter message again: ")

md5_digest_again = md5_hash(message_again)
print("MD5 hash of the entered message again:", md5_digest_again)

# Compare the calculated hash with the provided hash
if md5_digest == md5_digest_again:
    print("Hashes match: Message has not been altered.")
else:
    print("Hashes do not match: Message may have been altered.")
