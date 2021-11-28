from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

# Generate a new random private key for Bob (we call this a signing key)
bobs_private_key = SigningKey.generate()

# Sign a message with it
signed = bobs_private_key.sign(b'Attack at Dawn')

# Obtain the verification key for a given signing key
bobs_public_key = bobs_private_key.verify_key

# Serialize the verify key to send it to a third party
bobs_public_key_hex = bobs_public_key.encode(encoder=HexEncoder)

print(bobs_public_key_hex.decode('utf-8'))
