import networkx as nx
import matplotlib.pyplot as plt

g = {
    5: {3: 1, 8 :6},
    3: {2: 3, 4: 1},
    2: {},
    4: {8: 1},
    8: {9: 4}
}

for k, d in g.items():
    for ik in d:
        d[ik] = {'weight': d[ik]}
        
print(g)        

def UCS(g, initial, goal):
    visited=set()
    q=list()
    path = [initial]
    q.append([0, path])
    
    while q:
        q.sort()
        dis,path = q.pop(0)        
        s =path[len(path)-1]
        if s==goal:
            return [path, dis]
        visited.add(s)
        
        for n in g[s].keys():
            if n not in visited:
                newpath=list(path)
                newpath.append(n)
                q.append([dis + g[s][n]['weight'] , newpath])

G = nx.DiGraph(g)
pos = nx.spring_layout(G,k=.8)
nx.draw_networkx(G, pos)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

initial=5
goal=9

print(UCS(g,initial,goal))