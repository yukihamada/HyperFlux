import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f'Transaction({self.sender}, {self.receiver}, {self.amount}, {self.timestamp})'

    def is_valid(self):
        if self.amount <= 0:
            return False
        if not self.sender or not self.receiver:
            return False
        if not isinstance(self.amount, (int, float)):
            return False
        return True

    def zk_snark_proof(self):
        # Example zk-SNARK proof generation (simplified)
        g1 = G1
        g2 = G2
        proof = pairing(g1, g2) == pairing(h, g2)
        return proof

