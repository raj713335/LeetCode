# DFS-Based Path Existence

def path_exists_dfs(graph, src, dst, visited=None):
    if visited is None:
        visited = set()

    if src == dst:
        return True

    visited.add(src)
    for neighbor in graph[src]:
        if neighbor not in visited:
            if path_exists_dfs(graph, neighbor, dst, visited):
                return True

    return False


# BFS-Based Path Existence

from collections import deque

def path_exists_bfs(graph, src, dst):
    visited = set()
    queue = deque([src])

    while queue:
        node = queue.popleft()
        if node == dst:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

src = 0
dst = 3

print("DFS: Path exists?", path_exists_dfs(graph, src, dst))
print("BFS: Path exists?", path_exists_bfs(graph, src, dst))

