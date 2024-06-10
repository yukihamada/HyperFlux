from dag import DAG


class BFTNode:
    def __init__(self, node_id):
        """Initialize a BFT node."""
        self.node_id = node_id
        self.blockchain = []
        self.dag = DAG()
        self.wallet = 0  # ウォレットの初期残高

    def add_transaction(self, transaction):
        """Add a transaction to the node."""
        if transaction.is_valid() and transaction.zk_snark_proof():
            self.dag.add_transaction(transaction)
            print(f'Transaction added by node {self.node_id}')
        
        transactions = self.dag.get_transactions()
        for transaction in transactions:
            print(f'Processing transaction: {transaction}')
        
        # Mine a new block when a new transaction is added
        if len(transactions) > 0:
            previous_block = self.blockchain[-1] if self.blockchain else create_genesis_block()
            new_block = mine_block(previous_block, transactions, difficulty=4)
            self.receive_block(new_block)
            self.wallet += 50  # マイニング報酬をウォレットに追加
            print(f'Node {self.node_id} received mining reward. Wallet balance: {self.wallet}')

    def receive_block(self, block):
        """Receive a block and add it to the blockchain."""
        self.blockchain.append(block)
        if not is_chain_valid(self.blockchain):
            self.blockchain.pop()
            print(f'Invalid block received by node {self.node_id}')
        print(f'Block received and added by node {self.node_id}')



    def add_transaction(self, transaction):
        """Add a transaction to the node."""
        if transaction.is_valid() and transaction.zk_snark_proof():
            self.dag.add_transaction(transaction)
            print(f'Transaction added by node {self.node_id}')
        
        transactions = self.dag.get_transactions()
        for transaction in transactions:
            print(f'Processing transaction: {transaction}')
        
        # Mine a new block when a new transaction is added
        if len(transactions) > 0:
            previous_block = self.blockchain[-1] if self.blockchain else create_genesis_block()
            new_block = mine_block(previous_block, transactions, difficulty=4)
            self.receive_block(new_block)

    def receive_block(self, block):
        """Receive a block and add it to the blockchain."""
        self.blockchain.append(block)
        if not is_chain_valid(self.blockchain):
            self.blockchain.pop()
            print(f'Invalid block received by node {self.node_id}')
        print(f'Block received and added by node {self.node_id}')

