from nacl.public import PrivateKey, Box

# Generate key pairs for Alice and Bob
alices_secret_key = PrivateKey.generate()
bobs_secret_key = PrivateKey.generate()

# Extract public keys
alices_public_key = alices_secret_key.public_key
bobs_public_key = bobs_secret_key.public_key

# Bob wishes to send Alice an encrypted message using the Box class
bobs_box = Box(bobs_secret_key, alices_public_key)
secret_message = b'I am Satoshi'
encrypted = bobs_box.encrypt(secret_message)

# Alice creates a second Box to decrypt the message
alices_box = Box(alices_secret_key, bobs_public_key)

# An except will be raised if there was tampering or any other sort of error
plaintext = alices_box.decrypt(encrypted)
print(plaintext.decode('utf-8'))
