# https://leetcode.com/problems/unique-paths-ii/description/

# Time Complexity: O(m × n)
# Space Complexity: O(m × n) (for memo and recursion stack)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(i, j, memo = {}):

            if (i, j) in memo:
                return memo[i, j]

            elif i == 0 and j == 0:
                return 1 if  obstacleGrid[i][j] == 0 else 0
            
            elif i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            else:
                memo[i, j] = dfs(i-1, j, memo) + dfs(i, j-1, memo)
            return memo[i, j]

        return dfs(m-1, n-1)

