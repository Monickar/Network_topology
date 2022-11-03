import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([[1, 1, 0],[1, 0, 1]])

G = nx.
ax = plt.subplot(111)
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
nx.draw(G, pos=pos, ax=ax, with_labels = True)
plt.show()