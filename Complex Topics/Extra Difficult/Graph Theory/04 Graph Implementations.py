def build_graph(n, edges, directed=False):
    # Initialize adjacency list and matrix
    adj_list = {i: [] for i in range(n)}
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for u, v in edges:
        # Add to adjacency list
        adj_list[u].append(v)
        adj_matrix[u][v] = 1

        # If undirected, add reverse as well
        if not directed:
            adj_list[v].append(u)
            adj_matrix[v][u] = 1

    return adj_list, adj_matrix

def print_adj_list(adj_list):
    print("Adjacency List:")
    for node in adj_list:
        print(f"{node} -> {adj_list[node]}")
    print()

def print_adj_matrix(adj_matrix):
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(" ".join(map(str, row)))
    print()

# Example usage
if __name__ == "__main__":
    n = 5  # Number of nodes
    edges = [
        (0, 1),
        (0, 4),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (3, 4)
    ]

    adj_list, adj_matrix = build_graph(n, edges, directed=False)

    print_adj_list(adj_list)
    print_adj_matrix(adj_matrix)
