# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)

        for (x,y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1/value

        def bfs(x, y):

            if x not in graph or y not in graph:
                return -1

            q = deque()
            q.append((x, 1))

            visited = set()

            while q:
                
                node, product = q.popleft()

                if node == y:
                    return product 

                visited.add(node)

                for nei, value in graph[node].items():
                    if nei not in visited:
                        q.append((nei, product * value))


            return -1       

        res = []

        for x, y in queries:
            res.append(bfs(x, y))

        return res
