# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adjency_list = {}

        for edge in edges:
            if edge[0] not in adjency_list:
                adjency_list[edge[0]] = [edge[1]]
            else:
                adjency_list[edge[0]].append(edge[1])
            
            if edge[1] not in adjency_list:
                adjency_list[edge[1]] = [edge[0]]
            else:
                adjency_list[edge[1]].append(edge[0])

        visited = set()

        def dfs(source, destination):
            if source == destination:
                return True

            visited.add(source)
            for node in adjency_list[source]:
                if node not in visited:
                    if dfs(node, destination):
                        return True

            return False

        return dfs(source, destination)
