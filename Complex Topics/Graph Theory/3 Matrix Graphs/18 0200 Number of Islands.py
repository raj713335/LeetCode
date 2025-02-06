# https://leetcode.com/problems/number-of-islands/description/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        visited = set()

        isLandCount = 0


        def dfs(r, c):

            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for i in range(0, R):
            for j in range(0, C):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    isLandCount += 1

        return isLandCount  