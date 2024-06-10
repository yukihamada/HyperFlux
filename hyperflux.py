import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import argparse
import hashlib
import uuid
import asyncio
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request, jsonify
from bft_node import BFTNode
from blockchain import Block, calculate_hash, create_genesis_block, is_chain_valid
from transaction import Transaction
from dag import DAG

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

        if current_block.previous_hash != previous_block.hash:
            return False
        for transaction in current_block.transactions:
            if not transaction.is_valid():
                return False
        if not self.latest_status:
            return {
                "active_nodes": 0,
                "network_latency": 0.0,
                "tx_per_second": 0,
                "total_tx": 0
            }
        return self.latest_status

        return self.latest_status

        return self.latest_status


        return self.latest_status

        active_nodes = len(self.latest_status)
        total_latency = sum(status['latency'] for status in self.latest_status)
        total_tx_per_second = sum(status['tx_per_second'] for status in self.latest_status)
        total_tx = sum(status['total_tx'] for status in self.latest_status)
        return {
            "active_nodes": active_nodes,
            "network_latency": total_latency / active_nodes,
            "tx_per_second": total_tx_per_second / active_nodes,
            "total_tx": total_tx
        }

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

def generate_transaction_id():
    return str(uuid.uuid4())

def send_transaction(address, amount):
    transaction_id = generate_transaction_id()
    print("==================================================")
    print("取引送信:")
    print(f"送信先アドレス: {address}")
    print(f"送信するトークン量: {amount}")
    print("トランザクションを送信中...")
    print(f"トランザクションID: {transaction_id}")
    print("トランザクションが正常に送信されました。")
    print("==================================================")
    return transaction_id

def network_status(bft_network):
    status = bft_network.get_network_status()
    print("==================================================")
    print("ネットワークステータス:")
    print(f"アクティブノード数: {status['active_nodes']}")
    print(f"ネットワーク遅延: {status['network_latency']} ms")
    print(f"毎秒トランザクション数: {status['tx_per_second']}")
    print(f"総トランザクション数: {status['total_tx']}")
    print("==================================================")

    print("ネットワークステータス:")
    print(f"- アクティブノード数: {status['active_nodes']}")
    print(f"- ネットワーク遅延: 平均{status['network_latency']:.2f}ms")
    print(f"- トランザクション処理速度: 1秒間に{status['tx_per_second']:.2f}トランザクション")
    print(f"- 総トランザクション数: {status['total_tx']}")
    print("==================================================")

def display_node_status(node):
    status = node.get_status()
    print("Node status:")
    print("==================================================")
    print("State: Active")
    print(f"Number of connected peers: {status['connected_peers']}")
    print(f"Block Height: {status['block_height']}")
    print(f"Number of transactions: {status['total_tx']}")
    print(f"Memory Used: {status['memory_used']}MB")
    print(f"Uptime: {status['uptime']} hours")
    print("==================================================")

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

    return app

async def update_status(bft_network):
    while True:
        await bft_network.update_status()
        await asyncio.sleep(5)

async def cli_interface(bft_network):
    parser = argparse.ArgumentParser(description='HyperFlux Dashboard')
    parser.add_argument('choice', type=int, choices=range(1, 8), help='Select functionality (1-7)')
    args = parser.parse_args()

    node = bft_network.nodes[0]  # 表示用に最初のノードを使用

    print("==================================================")
    print("HyperFlux Status: Initializing...")
    print("[###----] Loading configuration...")
    print("[#####---] Connecting to network...")
    print("[########] Node started successfully...")
    print("==================================================")
    print("HyperFlux WEB interface: http://localhost:5000")
    print("==================================================")
    print("Dashboard:")
    print("1. 🚀 Check node status")
    print("2. 💸 Submit transaction")
    print("3. 🌐 Check network status")
    print("4. 📜 Smart contract management")
    print("5. 🗳️ Governance")
    print("6. 🌉 Cross-chain functionality")
    print("7. ⚙️ Configuration")
    print("==================================================")

    choice = args.choice

    if choice == 1:
        display_node_status(node)
    elif choice == 2:
        address = input("Recipient address: ")
        amount = input("Transfer amount: ")
        send_transaction(address, amount)
    elif choice == 3:
        network_status(bft_network)
    elif choice == 4:
        print("Smart contract management is not implemented yet.")
    elif choice == 5:
        print("Governance is not implemented yet.")
    elif choice == 6:
        print("Cross-chain functionality is not implemented yet.")
    elif choice == 7:
        print("Configuration is not implemented yet.")
    else:
        print("Invalid choice. Please select a number between 1 and 7.")


async def main():
    bft_network = BFTNetwork(num_nodes=200)  # ノード数を適宜設定

    app = create_app(bft_network)
    loop = asyncio.get_event_loop()

    # 非同期にステータスを更新
    loop.create_task(update_status(bft_network))

    # CLIインターフェースを非同期で実行
    loop.create_task(cli_interface(bft_network))

    # Flaskアプリケーションを実行
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    asyncio.run(main())

