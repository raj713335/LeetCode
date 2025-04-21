class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        memo = {}

        def dfs(l, r):

            if (l, r) in memo:
                return memo[(l, r)]

            if r - l == 1:
                return 0

            res = float("inf")

            for c in cuts:
                if l < c < r:
                    res = min(res, (r - l) + dfs(l, c) + dfs(c, r))

            memo[(l, r)] = res = 0 if res == float("inf") else res

            return res

        return dfs(0, n)

        
