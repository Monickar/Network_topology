import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#处理路由矩阵
def make_f(a, f):
    for i in range(5):
        j = 0
        slow = 0
        fast = 0
        #寻找第一个1
        while a[i,j] != 1:
            j += 1
        slow = j
        fast = j + 1
        while slow < 5 and fast < 8:
            if fast < 8 and a[i,fast] == 1 :
                f.append([slow + 1, fast + 1])
                slow = fast
                fast += 1
            else:
                fast += 1

    #嵌套去重
    f = [list(t) for t in set(tuple(_) for _ in f)]
    #排序
    f.sort()

# 画出拓扑树
def draw_pic(f):
    G = nx.Graph() 
    #添加节点
    for i in range(8):
        G.add_node(i+1)
    #添加边
    for i in range(len(f)):
        G.add_edges_from([(f[i][0],f[i][1])])

    ax = plt.subplot(111)
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw(G, pos = pos, ax = ax, with_labels = True)
    
    plt.show()

if __name__ == '__main__':
    
    a = np.array([[1,1,0,0,0,0,0,0],[1,0,1,0,1,0,0,0],
            [1,0,1,1,0,1,0,0],[1,0,1,1,0,0,1,0],
            [1,0,1,1,0,0,0,1]])
    f = []
    make_f(a, f)
    draw_pic(f)
