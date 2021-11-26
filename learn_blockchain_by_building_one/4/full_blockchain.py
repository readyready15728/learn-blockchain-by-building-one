import datetime
import hashlib
import json
import random

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create the genesis block
        print('Creating genesis block')
        self.new_block()

    def new_block(self, previous_hash=None):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'nonce': format(random.getrandbits(64), 'x')
        }

        # Get the hash of this new block and add it to the block
        block['hash'] = self.hash(block)

        # Reset the list of pending transactions
        self.pending_transactions = []
        # Add the block to the chain
        self.chain.append(block)

        print(f"Created block {block['index']}")
        return block

    @staticmethod
    def hash(block):
        # Ensure the dictionary is sorted or hashes will be inconsistent
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        # Returns the last block in the chain (if there are blocks)
        return self.chain[-1] if self.chain else None

    @staticmethod
    def valid_block(block):
        return block['hash'].startswith('0000')

    def proof_of_work(self):
        while True:
            new_block = self.new_block()

            if self.valid_block(new_block):
                break

        self.chain.append(new_block)
        print('Found a new block: ', new_block)
