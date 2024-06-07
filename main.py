import hashlib
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):


    def is_valid(self):
        # トランザクションの検証ロジックを追加
        return True








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
    value = f"{index}{previous_hash}{timestamp}{transactions}"
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


class ParallelTransactionProcessor:
    def __init__(self, dag, bft_network):
        self.dag = dag
        self.bft_network = bft_network

    def process_transactions(self, transactions):
        for transaction in transactions:
            self.dag.add_transaction(transaction)
        valid_transactions = self.dag.get_valid_transactions()
        return valid_transactions

class BFTNetwork:
    def __init__(self, num_nodes):
        self.nodes = [BFTNode(i) for i in range(num_nodes)]

    def broadcast_block(self, block):
        for node in self.nodes:
            node.receive_block(block)


    def get_valid_transactions(self):
        valid_transactions = []
        for node in self.nodes:
            if node.is_valid():
                valid_transactions.append(node.transaction)
        return valid_transactions


    def is_network_valid(self):
        for node in self.nodes:
            if not is_chain_valid(node.blockchain):
                return False
        return True

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
        valid_transactions = []
        for node in self.nodes:
            if node.is_valid():
                valid_transactions.append(node.transaction)
        return valid_transactions



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

def create_genesis_block():
    genesis_transactions = [Transaction('system', 'user', 50)]
    return Block(0, '0', int(time.time()), genesis_transactions, calculate_hash(0, '0', int(time.time()), genesis_transactions))

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

def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    transaction_pool = []
    dag = DAG()
    bft_network = BFTNetwork(num_nodes=5)
    processor = ParallelTransactionProcessor(dag, bft_network)

    num_of_blocks_to_add = 10

    for i in range(1, num_of_blocks_to_add + 1):
        transaction_pool.append(Transaction(f"user_{i}", f"user_{i+1}", i * 10))
        valid_transactions = processor.process_transactions(transaction_pool)
        block_to_add = mine_block(previous_block, valid_transactions, difficulty=2)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        transaction_pool = []
        bft_network.broadcast_block(block_to_add)
        print(f"Block #{block_to_add.index} has been added to the blockchain!")
        print(f"Hash: {block_to_add.hash}")
        print(f"Transactions: {[str(tx) for tx in block_to_add.transactions]}")

    print('Is BFT network valid?', bft_network.is_network_valid())

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

if __name__ == "__main__":
    main()