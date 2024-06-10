from bft_node import BFTNode
from blockchain import is_chain_valid

class BFTNetwork:
    def __init__(self, num_nodes):
        """Initialize a BFT network with a given number of nodes."""
        self.nodes = [BFTNode(i) for i in range(num_nodes)]

    def broadcast_block(self, block):
        """Broadcast a block to all nodes in the network."""
        for node in self.nodes:
            node.receive_block(block)

    def is_network_valid(self):
        """Check if the entire network's blockchain is valid."""
        for node in self.nodes:
            if not is_chain_valid(node.blockchain):
                return False
        return True

