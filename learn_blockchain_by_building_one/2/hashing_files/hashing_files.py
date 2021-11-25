import hashlib

# Slight change to an image results in vastly different hash
original_picture = 'undoctored-benjamin.png'
altered_picture = 'doctored-benjamin.png'

with open(original_picture, 'rb') as f:
    print(f'Hex digest of {original_picture}: {hashlib.sha256(f.read()).hexdigest()}')

with open(altered_picture, 'rb') as f:
    print(f'Hex digest of {altered_picture}: {hashlib.sha256(f.read()).hexdigest()}')
