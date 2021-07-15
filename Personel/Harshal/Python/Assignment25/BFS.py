visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue :
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {0:[1,2],2:[],1:[2],4:[3],6:[1,2],5:[3,7]}
print("\nFollowing is the Breadth First Search :")
bfs(visited,graph,0)
print("\n")

