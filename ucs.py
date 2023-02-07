import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge(0, 1, weight=2)
G.add_edge(0, 3, weight=5)
G.add_edge(1, 6, weight=1)
G.add_edge(3, 1, weight=5)
G.add_edge(3, 6, weight=6)
G.add_edge(3, 4, weight=2)
G.add_edge(6, 4, weight=7)
G.add_edge(5, 2, weight=6)
G.add_edge(5, 6, weight=3)
G.add_edge(4, 2, weight=4)
G.add_edge(2, 1, weight=4)
G.add_edge(4, 5, weight=3)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

q = []

source = 0
destination = 6

q.append(([source], 0))

print(q)

# while len(q) != 0: