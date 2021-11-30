import json
import structlog
from json.decoder import JSONDecodeError
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

logger = structlog.get_logger(__name__)
wallet_file = 'wallet.json'

def generate_wallet():
    private_key = SigningKey.generate()
    public_key = private_key.verify_key
    payload = {
        'private_key': private_key.encode(encoder=HexEncoder).decode(),
        'public_key': public_key.encode(encoder=HexEncoder).decode()
    }

    with open(wallet_file, 'w') as f:
        json.dump(payload, f)

    logger.info(f'Generated new wallet: {wallet_file}')

    return payload

try:
    with open(wallet_file) as f:
        keys = json.load(f)

    logger.info(f'Loaded keys from {wallet_file}')
except (JSONDecodeError, FileNotFoundError):
    keys = generate_wallet()

PRIVATE_KEY = keys['private_key']
PUBLIC_KEY = keys['public_key']
