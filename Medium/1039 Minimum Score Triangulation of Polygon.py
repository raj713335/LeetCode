# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        arr = values
        n = len(arr)
        dp = {}

        def solve(i, j):
            if i == j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            min_cost = float('inf')

            for k in range(i, j):
                cost = (
                    solve(i, k) +
                    solve(k + 1, j) +
                    arr[i - 1] * arr[k] * arr[j]
                )
                min_cost = min(min_cost, cost)

            dp[(i, j)] = min_cost
            return dp[(i, j)]

        return solve(1, n - 1)
        
