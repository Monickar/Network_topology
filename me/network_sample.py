import networkx as nx
import matplotlib.pyplot as plt
#更新全局参数，设置图形大小
# plt.rcParams.update({
#     'figure.figsize':(8,6)
# })
# 创建空的无向图
G = nx.Graph() 

G.add_node('Node1') # 一次添加一个节点(这里使用字母作为节点的id)
G.add_nodes_from(['Node2','Node3','Node4']) # 添加多个节点
# 添加一条线，连接Node1和Node2，
G.add_edge('Node1','Node2') 
# 同时添加多条线 
G.add_edges_from([('Node2','Node3'),('Node2','Node4'),('Node4','Node3')]) 
G.add_edges_from([('Node3', 'X'), ('Node2', 'T')])
nx.draw_networkx(G)
plt.show()