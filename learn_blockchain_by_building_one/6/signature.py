from nacl.encoding import HexEncoder
from nacl.signing import SigningKey, VerifyKey

# Generate a new random private key for Bob (we call this a signing key)
bobs_private_key = SigningKey.generate()

# Sign a message with it
signed = bobs_private_key.sign(b'Attack at Dawn')

# Obtain the verification key for a given signing key
bobs_public_key = bobs_private_key.verify_key

# Serialize the verify key to send it to a third party
bobs_public_key_hex = bobs_public_key.encode(encoder=HexEncoder)

# Now, sign a message with Bob's private key
signed_message = bobs_private_key.sign(b'Send $37 to Alice')
print('Signed message:', signed_message)

# And verify the key
verify_key = VerifyKey(bobs_public_key_hex, encoder=HexEncoder)
print('Verification attempt:', verify_key.verify(signed_message))
