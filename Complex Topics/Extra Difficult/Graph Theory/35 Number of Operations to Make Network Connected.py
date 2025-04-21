# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        adjency_list = defaultdict(list)

        for u, v in connections:
            adjency_list[u].append(v)
            adjency_list[v].append(u)


        def dfs(i):

            visited.add(i)

            for nei in adjency_list[i]:
                if nei not in visited:
                    dfs(nei)



        components = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1


        return components - 1
        
