
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

