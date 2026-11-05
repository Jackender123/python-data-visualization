import networkx as nx
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tạo đồ thị
# plt.figure(figsize=(6, 4)): Tạo vùng vẽ rộng 6 inch và cao 4 inch
# sns.heatmap(...): Vẽ ma trận dưới dạng bản đồ nhiệt.
# adj_matrix: Ma trận dữ liệu cần trực quan hóa.
# cmap='YlGnBu': Chọn bảng màu chuyển từ vàng sang xanh lá và xanh dương.
# annot=True: Hiển thị giá trị số trong từng ô.
# plt.title(...): Đặt tiêu đề.
#plt.show(): Hiển thị biểu đồ.

G = nx.cycle_graph(5)
labels = {i: f"Node {i}" for i in G.nodes()}
adj_matrix = nx.to_pandas_adjacency(G)
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
# Vẽ heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(adj_matrix, cmap='YlGnBu', annot=True)
plt.title("Ma trận kề của chu trình 5 nút")
plt.show()