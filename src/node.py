
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from bft_node import BFTNode
from blockchain import Block, calculate_hash, create_genesis_block, is_chain_valid
from transaction import Transaction
from dag import DAG
import asyncio
from flask import Flask, render_template, request, jsonify
from concurrent.futures import ThreadPoolExecutor

class BFTNetwork:
    def __init__(self, num_nodes):
        """Initialize a BFT network with a given number of nodes."""
        self.nodes = [BFTNode(i) for i in range(num_nodes)]
        self.executor = ThreadPoolExecutor(max_workers=num_nodes)
        self.latest_status = None

    async def update_status(self):
        """Periodically update the status of the network."""
        while True:
            self.latest_status = await self.collect_status()
            await asyncio.sleep(5)  # Update every 5 seconds

    async def collect_status(self):
        """Collect the status from all nodes in the network."""
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(self.executor, node.get_status) for node in self.nodes]
        statuses = await asyncio.gather(*tasks)
        return statuses

    def broadcast_block(self, block):
        """Broadcast a block to all nodes in the network."""
        for node in self.nodes:
            node.receive_block(block)

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

async def main():
    bft_network = BFTNetwork(num_nodes=200)  # ノード数を適宜設定

    app = create_app(bft_network)
    loop = asyncio.get_event_loop()

    # 非同期にステータスを更新
    loop.create_task(bft_network.update_status())

    # Flaskアプリケーションを実行
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    asyncio.run(main())

