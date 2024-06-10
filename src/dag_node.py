class DAGNode:
    def __init__(self, transaction):
        """Initialize a DAG node."""
        self.transaction = transaction
        self.parents = []

    def add_parent(self, parent_node):
        """Add a parent node to the DAG node."""
        self.parents.append(parent_node)

    def is_valid(self):
        """Check if the DAG node is valid."""
        if not self.transaction.is_valid():
            return False
        for parent in self.parents:
            if not parent.is_valid():
                return False
        return True

