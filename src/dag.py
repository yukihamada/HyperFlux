import networkx as nx

class DAG:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_transaction(self, transaction):
        self.graph.add_node(transaction)

    def add_dependency(self, transaction1, transaction2):
        self.graph.add_edge(transaction1, transaction2)

    def get_transactions(self):
        return list(nx.topological_sort(self.graph))

