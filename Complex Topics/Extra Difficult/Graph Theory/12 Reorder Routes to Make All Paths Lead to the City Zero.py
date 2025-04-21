# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adjancy_list = defaultdict(list)
        graph_direction = set()

        for edge in connections:

            adjancy_list[edge[0]].append(edge[1])
            adjancy_list[edge[1]].append(edge[0])
            graph_direction.add((edge[0], edge[1]))
     
        
        visited = set()
        count = 0
        
        def bfs(start):

            visited = set()
            count = 0

            q = deque()
            q.append(start)

            while q:

                city_node = q.popleft()
                visited.add(city_node)

                for node in adjancy_list[city_node]:
                    if node not in visited:
                        if (city_node, node) in graph_direction:
                            count += 1
                        q.append(node)

            return count

        return bfs(0)

        

            
