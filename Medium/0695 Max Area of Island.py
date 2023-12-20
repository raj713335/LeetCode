# https://leetcode.com/problems/max-area-of-island/description/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_row = len(grid)
        max_col = len(grid[0])

        visited = set()

        max_area = 0

        def dfs(r, c):

            if r >= max_row or r < 0 or c >= max_col or c < 0 or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            if grid[r][c] == 1:
                return (1+
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1))

        isLand = 0

        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    isLand = dfs(i, j)
                    max_area = max(max_area, isLand)

        return max_area
        
