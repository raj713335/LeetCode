# https://leetcode.com/problems/number-of-enclaves/description/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        max_row = len(grid)
        max_col = len(grid[0])

        visited = set()

        def dfs(r, c):

            if r >= max_row or r < 0 or c >= max_col or c < 0 or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            res = 1

            res += dfs(r+1, c)
            res += dfs(r-1, c)
            res += dfs(r, c+1)
            res += dfs(r, c-1)

            return res

        land, borderLand = 0, 0

        for i in range(0, max_row):
            for j in range(0, max_col):
                land += grid[i][j]
                if (grid[i][j] and (i, j) not in visited and (i == 0 or i == (max_row-1)) or (j == 0 or j == (max_col-1))):
                    borderLand += dfs(i, j)


        print(land, borderLand)
        return land-borderLand

        
