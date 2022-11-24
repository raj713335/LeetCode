# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]

        return res
        
