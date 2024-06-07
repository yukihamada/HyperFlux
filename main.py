import hashlib
import time

class DAG:
    def __init__(self):
        self.nodes = []

    def add_transaction(self, transaction):
        new_node = DAGNode(transaction)
        for node in self.nodes:
            if node.is_valid():
                new_node.add_parent(node)
        self.nodes.append(new_node)

    def get_valid_transactions(self):
        return [node.transaction for node in self.nodes if node.is_valid()]

class DAGNode:
    def __init__(self, transaction):
        self.transaction = transaction
        self.parents = []

    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    def is_valid(self):
        # トランザクションの検証ロジックを追加
        return self.transaction.is_valid()

class BFTNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = []

    def receive_block(self, block):
        self.blockchain.append(block)

    def is_block_valid(self, block):
        # ブロックの検証ロジックを追加
        return True

    def broadcast_block(self, block, nodes):
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_block(block)

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
def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    transaction_pool = TransactionPool()
    dag = DAG()

    num_of_blocks_to_add = 10

    for i in range(1, num_of_blocks_to_add + 1):
        transaction_pool.add_transaction(Transaction(f"user_{i}", f"user_{i+1}", i * 10))
        transactions = transaction_pool.get_transactions()
        for transaction in transactions:
            dag.add_transaction(transaction)
        valid_transactions = dag.get_valid_transactions()
        block_to_add = mine_block(previous_block, valid_transactions, difficulty=2)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        transaction_pool.clear()
        print(f"Block #{block_to_add.index} has been added to the blockchain!")
        print(f"Hash: {block_to_add.hash}")
        print(f"Transactions: {[str(tx) for tx in block_to_add.transactions]}")
    return blockchain


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
    prefix_str = '0' * difficulty
    while True:
        hash = calculate_hash(index, previous_block.hash, timestamp, transactions + [nonce])
        if hash[:difficulty] == prefix_str:
            return Block(index, previous_block.hash, timestamp, transactions, hash)
        nonce += 1

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

