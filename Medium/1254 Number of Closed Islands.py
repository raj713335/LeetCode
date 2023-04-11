# https://leetcode.com/problems/number-of-closed-islands/


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == row or c == col):
                return 0
            if grid[r][c] == 1 or (r, c) in visited:
                return 1

            visited.add((r,c))

            return min(dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1))




        res = 0
        for r in range(0, row):
            for c in range(0, col):
                if grid[r][c] != 1 and (r,c) not in visited:
                    res += dfs(r, c)

        return res
