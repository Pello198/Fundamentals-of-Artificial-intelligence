# A* Search Algorithm in Python

# Graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

def search (start, goal):

    # Open list stores nodes to be explored
    open_list = [start]

    # Closed list stores visited nodes
    closed_list = []

    # Cost from start to node
    g = {}
    g[start] = 0

    # Parent nodes for path reconstruction
    parent = {}
    parent[start] = start

    while open_list:

        # Find node with lowest f(n)
        current = open_list[0]

        for node in open_list:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        # Goal test
        if current == goal:

            path = []

            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            print("Optimal Path:", path)
            return

        # Move current node from open to closed
        open_list.remove(current)
        closed_list.append(current)

        # Explore neighbors
        for neighbor, cost in graph[current]:

            if neighbor not in open_list and neighbor not in closed_list:

                open_list.append(neighbor)

                parent[neighbor] = current
                g[neighbor] = g[current] + cost

            else:

                if g[neighbor] > g[current] + cost:

                    g[neighbor] = g[current] + cost
                    parent[neighbor] = current

                    if neighbor in closed_list:
                        closed_list.remove(neighbor)
                        open_list.append(neighbor)

# Run algorithm
search('A', 'G')