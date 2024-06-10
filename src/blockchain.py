
def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        if current_block.previous_hash != previous_block.hash:
            return False
        if not current_block.has_valid_transactions():
            return False
    return True


import time

def create_genesis_block():
    genesis_transactions = [Transaction('system', 'user', 50)]
    return Block(0, '0', int(time.time()), genesis_transactions, calculate_hash(0, '0', int(time.time()), genesis_transactions))

import hashlib

def calculate_hash(index, previous_hash, timestamp, transactions):
    value = str(index) + previous_hash + str(timestamp) + str(transactions)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash

    def has_valid_transactions(self):
        # トランザクションの検証ロジックを追加
        return all(transaction.is_valid() for transaction in self.transactions)



from transaction import Transaction
import asyncio

def create_app(bft_network):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/node_status')
    def node_status():
        node = bft_network.nodes[0]
        status = node.get_status()
        return jsonify(status)

    @app.route('/network_status')
    def network_status():
        status = bft_network.get_network_status()
        return jsonify(status)

    @app.route('/send_transaction', methods=['POST'])
    def send_transaction():
        address = request.form['address']
        amount = request.form['amount']
        transaction = Transaction(sender="system", receiver=address, amount=float(amount))
        if transaction.is_valid() and transaction.zk_snark_proof():
            bft_network.nodes[0].add_transaction(transaction)
            return jsonify({"status": "success", "transaction_id": str(transaction)})
        else:
            return jsonify({"status": "failure", "message": "Invalid transaction"})

    return app

async def update_status(bft_network):
    while True:
        await bft_network.update_status()
        await asyncio.sleep(5)

        return False
    return True

