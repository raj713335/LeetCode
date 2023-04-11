# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        visited = set()


        def dfs(r, c):
            if (r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0):
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))

            peri = dfs(r+1, c)
            peri += dfs(r-1, c) 
            peri += dfs(r, c+1)
            peri += dfs(r, c-1)
            return peri



        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return dfs(r,c)



