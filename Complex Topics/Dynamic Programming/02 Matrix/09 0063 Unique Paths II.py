# https://leetcode.com/problems/unique-paths-ii/description/

# Time Complexity: O(m × n)
# Space Complexity: O(m × n) (for memo and recursion stack)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(i, j, memo = {}):
            if (i, j) in memo:
                return memo[i, j]
            if i == m-1 and j == n-1:
                return 1 if  obstacleGrid[i][j] == 0 else 0
            
            if i < 0 or i >= m or j < 0 or j >= n or obstacleGrid[i][j] == 1:
                return 0
            else:
                memo[i, j] = dfs(i+1, j, memo) + dfs(i, j+1, memo)
            return memo[i, j]

        return dfs(0, 0)
