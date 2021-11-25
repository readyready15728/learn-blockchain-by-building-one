import hashlib

secret_phrase = 'bolognese'

def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return hashlib.sha256(combined.encode()).hexdigest()

email_body = 'Hey Bob, I think you should learn about Blockchains! ' \
        'I\'ve been investing in Bitcoin and currently have exactly 12.03 BTC in my account.'

print('E-mail hash: ' + get_hash_with_secret_phrase(email_body, secret_phrase))
