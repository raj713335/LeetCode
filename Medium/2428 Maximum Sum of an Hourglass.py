# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        max_sum = 0

        for i in range(0, len(grid)-2):
            for j in range(0, len(grid[0])-2):
                temp = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                temp += grid[i+1][j+1]
                temp += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                if temp > max_sum:
                    max_sum = temp

        return max_sum
        
