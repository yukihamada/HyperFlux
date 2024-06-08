
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
from hyperflux import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_valid(self):
        tx = Transaction(sender="Alice", receiver="Bob", amount=10)
        self.assertTrue(tx.is_valid())

    def test_transaction_invalid_amount(self):
        tx = Transaction(sender="Alice", receiver="Bob", amount=-10)
        self.assertFalse(tx.is_valid())

    def test_transaction_invalid_sender_receiver(self):
        tx = Transaction(sender="", receiver="Bob", amount=10)
        self.assertFalse(tx.is_valid())
        tx = Transaction(sender="Alice", receiver="", amount=10)
        self.assertFalse(tx.is_valid())

if __name__ == '__main__':
    unittest.main()

