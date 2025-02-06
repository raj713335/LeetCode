# https://leetcode.com/problems/all-paths-from-source-to-target/description/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        path = []
        graph_len = len(graph)

        def dfs_terminiting(state, local_path):
            if state == graph_len - 1:
                path.append(local_path[:])
                return

            for j in range(0, len(graph[state])):
                local_path.append(graph[state][j])
                dfs_terminiting(graph[state][j], local_path)
                local_path.pop()

        dfs_terminiting(0, [0])

        return path
        
