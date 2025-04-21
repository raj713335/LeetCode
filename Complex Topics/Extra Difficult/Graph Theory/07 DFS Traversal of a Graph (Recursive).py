def dfs(graph, node, visited, traversal_order):
    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)

# Example graph (adjacency list)
graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

# DFS from node 0
visited = set()
traversal_order = []
dfs(graph, 0, visited, traversal_order)

print("DFS Traversal starting from node 0:")
print(traversal_order)
