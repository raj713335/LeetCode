# https://leetcode.com/problems/find-eventual-safe-states/description/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        graph_len = len(graph)
        memo = {}  # Use a dictionary to store True (safe) or False (unsafe)

        def dfs_terminating(state, visited):
            if state in memo:
                return memo[state]  # Return precomputed result

            if state in visited:
                return False  # Cycle detected, unsafe node

            visited.add(state)

            for neighbor in graph[state]:
                if not dfs_terminating(neighbor, visited):
                    memo[state] = False  # If any path leads to a cycle, it's unsafe
                    return False

            visited.remove(state)  # Remove from visited for backtracking
            memo[state] = True  # Mark as safe
            return True

        safe_nodes = []
        for i in range(graph_len):
            if dfs_terminating(i, set()):
                safe_nodes.append(i)

        return safe_nodes



