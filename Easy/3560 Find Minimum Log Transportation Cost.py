# https://leetcode.com/problems/find-minimum-log-transportation-cost/description/

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:

        if n == 0 or m == 0 or k == 0:
            return 0

        ans = 0

        if m <= k and n <= k:
            return 0

        if m > k and n <= k:
            ans += (m - k) * k
        if n > k and m <= k:
            ans += (n - k) * k


        return ans
        
