# https://leetcode.com/problems/strange-printer/description/

class Solution:
    def strangePrinter(self, s: str) -> int:

        dp = {}

        def mcm(i, j):

            if i > j:
                return 0
            if i == j:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            # Start with worst case: print s[i] separately and then rest
            res = mcm(i, j - 1) + 1

            for k in range(i, j):
                if s[k] == s[j]:
                    # We can merge the turn for s[j] with the one for s[k]
                    res = min(res, mcm(i, k) + mcm(k + 1, j - 1))

            dp[(i, j)] = res
            return dp[(i, j)]

        return mcm(0, len(s)-1)

        
