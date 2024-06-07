import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.amount}"

class Block:

    def __init__(self, index, previous_hash, timestamp, transactions, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions





def create_genesis_block():

    genesis_transactions = [Transaction("system", "user", 50)]
    return Block(0, "0", int(time.time()), genesis_transactions, calculate_hash(0, "0", int(time.time()), genesis_transactions))

def create_new_block(previous_block, transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, transactions)
    return Block(index, previous_block.hash, timestamp, transactions, hash)


def main():

    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_add = 10

    for i in range(1, num_of_blocks_to_add + 1):
        transactions = [Transaction(f"user_{i}", f"user_{i+1}", i * 10)]
        block_to_add = create_new_block(previous_block, transactions)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print(f"Block #{block_to_add.index} has been added to the blockchain!")
        print(f"Hash: {block_to_add.hash}")
        print(f"Transactions: {[str(tx) for tx in block_to_add.transactions]}")
    return blockchain



def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.transactions):
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

    return True


if __name__ == "__main__":
    blockchain = main()
    print("Is blockchain valid?", is_chain_valid(blockchain))

