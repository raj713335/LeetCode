# https://leetcode.com/problems/number-of-provinces/description/


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cities_len = len(isConnected)
        provience = 0
        visited = set()

        def dfs(start):

            visited.add(start)

            for i in range(0, cities_len):
                if isConnected[start][i] == 1 and i not in visited:
                    dfs(i)

        for i in range(0, cities_len):
                if i not in visited:
                    dfs(i)
                    provience += 1

        return provience
        