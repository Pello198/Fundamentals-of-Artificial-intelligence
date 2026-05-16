
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, goal, path)

            if new_path:
                return new_path

    return None


result = dfs(graph, 'A', 'F')

print("DFS Search Path:", result)