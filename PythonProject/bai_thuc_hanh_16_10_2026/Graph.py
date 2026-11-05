import networkx as nx
import matplotlib.pyplot as plt
#1 tao do thi don gian
G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])
#2 ve do thi 
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
plt.title("Đồ thị đơn giản")
plt.show()