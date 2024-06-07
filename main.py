import hashlib
import time

class TransactionPool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def clear(self):
        self.transactions = []

    def get_transactions(self):
        return self.transactions

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def is_valid(self):
        return self.sender != self.recipient and self.amount > 0
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

def mine_block(previous_block, transactions, difficulty):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0
    while True:
        hash = calculate_hash(index, previous_block.hash, timestamp, transactions + [nonce])
        if hash[:difficulty] == '0' * difficulty:
            return Block(index, previous_block.hash, timestamp, transactions, hash)
        nonce += 1




def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    transaction_pool = TransactionPool()

    num_of_blocks_to_add = 10

    for i in range(1, num_of_blocks_to_add + 1):
        transaction_pool.add_transaction(Transaction(f"user_{i}", f"user_{i+1}", i * 10))
        transactions = transaction_pool.get_transactions()
        block_to_add = mine_block(previous_block, transactions, difficulty=2)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        transaction_pool.clear()
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

        for transaction in current_block.transactions:
            if not transaction.is_valid():
                return False

    return True

    return True


if __name__ == "__main__":
    blockchain = main()
    print("Is blockchain valid?", is_chain_valid(blockchain))

