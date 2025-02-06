# https://leetcode.com/problems/pacific-atlantic-water-flow/description/


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        R = len(heights)
        C = len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()

        res = []

        def dfs(r, c, visited, prev):

            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or heights[r][c] < prev:
                return 

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        for r in range(0, R):
            dfs(r, 0, pacific_visited, heights[r][0])
            dfs(r, C-1, atlantic_visited, heights[r][C-1])

        for c in range(0, C):
            dfs(0, c, pacific_visited, heights[0][c])
            dfs(R-1, c, atlantic_visited, heights[R-1][c])

        for r in range(0, R):
            for c in range(0, C):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append([r, c])

        return res
