from blockchain import is_chain_valid

class BFTNode:
    def __init__(self, node_id):
        """Initialize a BFT node."""
        self.node_id = node_id
        self.blockchain = []

    def add_transaction(self, transaction):
        """Add a transaction to the node."""
        if transaction.is_valid() and transaction.zk_snark_proof():
            self.dag.add_transaction(transaction)
            print(f'Transaction added by node {self.node_id}')

        transactions = self.dag.get_transactions()
        for transaction in transactions:
            print(f'Processing transaction: {transaction}')
            print(f'Invalid transaction received by node {self.node_id}')

    def receive_block(self, block):
        """Receive a block and add it to the blockchain."""
        self.blockchain.append(block)
        if not is_chain_valid(self.blockchain):
            self.blockchain.pop()
            print(f'Invalid block received by node {self.node_id}')
        print(f'Block received and added by node {self.node_id}')

