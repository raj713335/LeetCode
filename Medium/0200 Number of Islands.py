# https://leetcode.com/problems/number-of-islands/description/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        max_row = len(grid)
        max_col = len(grid[0])

        visited = set()

        def dfs(r, c):

            if r >= max_row or r < 0 or c >= max_col or c < 0 or grid[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))

            if grid[r][c] == "1":
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        isLand = 0

        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    isLand += 1
                dfs(i,j)

        return isLand
