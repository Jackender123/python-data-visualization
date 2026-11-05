#Bai 5 dung force-directed layout de hien thi mang ngau nhien
import networkx as nx # thu vien dung de tao, phan tich ba truc quan hoa do thi 
import matplotlib.pyplot as plt # thu vien dung de tao  vung ve, dat tieu de va hien thi hinh anh 
#as nx,as plt: tao bi danh giup viet cide ngan gon
#Tao mang ngau nhien
#ham nx.gnp_random_graph(n,p,seed) tao mot do thi ngau nhien theo mo hinh G(n,p)
#seed=42 co dinh qua trinh sinh ngau nhien de de tai lap ket qua
G=nx.gnp_random_graph(10,0.3,seed=42) 
#Bo tri cac nut bang thuat toan luc
pos=nx.spring_layout(G)# tinh toan toa do hai chieu cho tung nut dua tren mo hinh luc
pos=nx.circular_layout(G) # sap xep cac nut theo hinh tron

#Ve 
plt.figure(figsize=(6,4))
nx.draw(G,pos,with_labels=True,node_color='lightgreen',node_size=800,font_size=10)
plt.title("force-directed layout cho mang ngau nhien")
plt.show()
