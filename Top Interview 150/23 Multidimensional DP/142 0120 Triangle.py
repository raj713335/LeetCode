# https://leetcode.com/problems/triangle/description/

# Time Complexity: O(m²)
# Space Complexity: O(n)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle[-1])

        dp = [0] * (n+1)

        triangle = triangle[::-1]

        for tri in triangle:
            for i in range(0, len(tri)):
                dp[i] = tri[i] + min(dp[i], dp[i+1])

        return dp[0]
