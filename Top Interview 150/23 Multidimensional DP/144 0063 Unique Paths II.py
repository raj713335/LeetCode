# https://leetcode.com/problems/unique-paths-ii/description/

# Time Complexity: O(m × n)
# Space Complexity: O(m × n) (for memo and recursion stack)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(m, n, memo={}):

            if (m,n) in memo:
                return memo[m,n]
            elif m == 0 and n == 0:
                return 1 if obstacleGrid[m][n] == 0 else 0
            elif m < 0 or n < 0 or obstacleGrid[m][n] == 1:
                return 0
            else:
                memo[m,n] = dfs(m-1,n, memo) + dfs(m, n-1, memo)
            return memo[m, n]

        return dfs(m-1, n-1)
            
