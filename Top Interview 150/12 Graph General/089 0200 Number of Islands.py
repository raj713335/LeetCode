# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        max_row = len(grid)
        max_col = len(grid[0])

        visited = set()

        island_count = 0

        def dfs(r, c):

            if r < 0 or r >= max_row or c < 0 or c >= max_col or (r, c) in visited or grid[r][c] == "0":
                return 

            visited.add((r, c))

            if grid[r][c] == "1":
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)


        for i in range(0, max_row):
            for j in range(0, max_col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island_count += 1
                dfs(i, j)

        return island_count
        
