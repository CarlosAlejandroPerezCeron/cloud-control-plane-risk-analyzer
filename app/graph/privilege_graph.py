import networkx as nx

def build_privilege_graph(identity, actions):
    graph = nx.DiGraph()
    graph.add_node(identity)

    for action in actions:
        graph.add_node(action)
        graph.add_edge(identity, action)

    return graph
