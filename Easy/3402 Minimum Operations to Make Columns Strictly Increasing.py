# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        count = 0

        for i in range(0, len(grid[0])):
            prev = grid[0][i]
            for j in range(1, len(grid)):
                if grid[j][i] <= prev:
                    val = (prev - grid[j][i]) + 1
                    grid[j][i] += val
                    count += val
                prev = grid[j][i]

        return count
