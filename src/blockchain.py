import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash

    def __repr__(self):
        return f"Block({self.index}, {self.previous_hash}, {self.timestamp}, {self.transactions}, {self.hash})"



def calculate_hash(index, previous_hash, timestamp, transactions):

    try:

        value = f"{index}{previous_hash}{timestamp}{transactions}"

        return hashlib.sha256(value.encode()).hexdigest()

    except Exception as e:

        print(f"Error calculating hash: {e}")

        return None



def create_genesis_block():
    return Block(0, '0', int(time.time()), [], calculate_hash(0, '0', int(time.time()), []))

def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.transactions):
            return False
        if current_block.previous_hash != previous_block.hash:
            return False
        for transaction in current_block.transactions:
            if not transaction.is_valid():
                return False
    return True

