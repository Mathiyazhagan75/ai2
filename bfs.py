import networkx as nx

def BFS(graph, index, target):
    queue = []
    queue.append(index)
    visited[index] = True
    
    while queue:
        index = queue.pop(0)
        
        print(index)
        route.append(index)
        
        if index == target:
            return
        
        for x in graph[index]:
            if(visited[x] == False):
                queue.append(x)
                visited[x] = True


def findPaths(route):
    paths = []
    for i in range(1, len(route)):
        path = [route[i-1], route[i]]
        paths.append(path)
    return paths

graph = {
    
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
    
    }

print("Graph: ", graph)

visited = [False for _ in range(len(graph))]

start = 0
target = 3

route = []

BFS(graph, start, target)

paths = findPaths(route)

G = nx.Graph()

for x in graph:
    G.add_node(x)
    
for x in graph:
    for y in graph[x]:
        G.add_edge(x, y)

pos = nx.spring_layout(G)

nx.draw(G, pos)

nx.draw_networkx_edges(G, pos, edgelist = paths, width = 3, edge_color='r')
