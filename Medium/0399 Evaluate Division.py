# https://leetcode.com/problems/evaluate-division/description/


import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)

        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val

        
        def bfs(x, y):

            if x not in graph or y not in graph:
                return -1.0

            visited = set()
            q = collections.deque([(x, 1)])

            while q:
                node, product = q.popleft()

                visited.add(node)

                if node == y:
                    return product

                for node, value in graph[node].items():
                    if node not in visited:
                        q.append((node, product * value))

            return -1.0

        res = []

        for (x, y) in queries:
            res.append(bfs(x, y))

        return res
        
