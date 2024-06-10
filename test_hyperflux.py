
import unittest
import time






class TestHyperFlux(unittest.TestCase):

    def test_transaction_validation(self):
        valid_transaction = Transaction('user_1', 'user_2', 10)
        invalid_transaction = Transaction('user_1', 'user_2', -10)
        self.assertTrue(valid_transaction.is_valid())
        self.assertFalse(invalid_transaction.is_valid())

    def test_block_creation(self):
        genesis_block = create_genesis_block()
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.previous_hash, '0')
        self.assertTrue(is_chain_valid([genesis_block]))

    def test_blockchain_validation(self):
        genesis_block = create_genesis_block()
        blockchain = [genesis_block]
        new_block = Block(1, genesis_block.hash, int(time.time()), [Transaction('user_1', 'user_2', 10)], 'dummy_hash')
        blockchain.append(new_block)
        self.assertFalse(is_chain_valid(blockchain))  # Invalid hash should make the chain invalid

if __name__ == '__main__':
    unittest.main()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import unittest
from hyperflux import Transaction, DAG, create_genesis_block, Block, calculate_hash

class TestTransaction(unittest.TestCase):
    def test_transaction_valid(self):
        tx = Transaction(sender="Alice", receiver="Bob", amount=10)
        self.assertTrue(tx.is_valid())

    def test_transaction_invalid_amount(self):
        tx = Transaction(sender="Alice", receiver="Bob", amount=-10)
        self.assertFalse(tx.is_valid())

        return True
        return True
        self.assertFalse(tx.is_valid())

    def test_zk_snark_proof(self):
        tx = Transaction(sender="Alice", receiver="Bob", amount=10)
        self.assertTrue(tx.zk_snark_proof())

    def test_dag_parallel_processing(self):
        dag = DAG()
        tx1 = Transaction(sender="Alice", receiver="Bob", amount=10)
        tx2 = Transaction(sender="Bob", receiver="Charlie", amount=5)
        dag.add_transaction(tx1)
        dag.add_transaction(tx2)
        transactions = dag.get_transactions()
        self.assertEqual(len(transactions), 2)

