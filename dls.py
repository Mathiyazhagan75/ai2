import networkx as nx

def DLS(graph, index, target, depth):
    if visited[index] == False:
        visited[index] = True
    
    route.append(index)
    
    if depth > limit:
        return False
    
    if(target == index):
        return True
    
    for i in graph[index]:
        if(visited[i] == False):
            if DLS(graph, i, target, depth+1):
                return True
            else:
                visited[i] = False
                route.pop()
                
    return False

def findPaths(route):
    paths = []
    for i in range(1, len(route)):
        path = [route[i-1], route[i]]
        paths.append(path)
    return paths

graph = {
    
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 5],
    3: [0, 6],
    4: [2, 7],
    5: [3, 7],
    6: [4, 7],
    7: [4, 5, 6]
    
    }

print("Graph: ", graph)

visited = [False for _ in range(len(graph))]

start = 6
target = 7

route = []

limit = 2

DLS(graph, start, target, 0)

if visited[target] == False:
    print("Path doesn't exist within given limit")
else:
    print(route)
    

paths = findPaths(route)

G = nx.Graph()

for x in graph:
    G.add_node(x)
    
for x in graph:
    for y in graph[x]:
        G.add_edge(x, y)

pos = nx.spring_layout(G)

nx.draw_networkx(G, pos)

nx.draw_networkx_edges(G, pos, edgelist = paths, width = 3, edge_color='r')

