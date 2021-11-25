import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create the genesis block
        print('Creating genesis block')
        self.new_block()

    def new_block(self, previous_hash=None):
        # Generates a new block and adds it to the chain
        block = {
            'index': len(self.chain),
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash
        }

        # Get the hash of this new block, and add it to the block
        block['hash'] = self.hash(block)

        # Reset the list of pending transactions
        self.pending_transactions = []
        # Add the block to the chain
        self.chain.append(block)

        print(f"Created block {block['index']}")
        return block

    @staticmethod
    def hash(block):
        # Hashes a Block

        # Ensure the dictionary is sorted or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        # Gets the latest Block in the chain (if there are any)
        return self.chain[-1] if len(self.chain) > 0 else None

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of pending transactions

        self.pending_transactions.append({
            'recipient': recipient,
            'sender': sender,
            'amount': amount
        })
