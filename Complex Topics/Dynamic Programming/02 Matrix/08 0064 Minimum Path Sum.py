# https://leetcode.com/problems/minimum-path-sum/description/


# Time Complexity: O(m × n) (where m is ROW and n is COL)
# Space Complexity: O(m × n) (can be optimized to O(n))


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        res = [[float("inf")] * (COL+1) for c in range(0, ROW+1)]

        res[ROW-1][COL] = 0

        for i in range(ROW-1, -1, -1):
            for j in range(COL-1, -1, -1):
                res[i][j] = grid[i][j] + min(res[i+1][j], res[i][j+1])

        return res[0][0]



# Time Complexity: O(m × n)
# Space Complexity: O(m × n) (due to memo storage and recursion stack)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def minPathSum(grid, i=0, j=0, memo ={}):

            if (i, j) in memo:
                return memo[i, j]

            # Base case: If we reach the bottom-right cell, return its value
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            # If we go out of bounds, return a large number
            if i >= m or j >= n:
                return float('inf')
            
            # Recursive case: Move right and down, then take the minimum
            memo[i, j] = grid[i][j] + min(minPathSum(grid, i+1, j), minPathSum(grid, i, j+1))

            return memo[i, j]

        return minPathSum(grid)
