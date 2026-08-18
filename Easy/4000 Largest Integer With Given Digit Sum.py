# https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution:
    def largestInteger(self, n: int, s: int) -> int:

        if 9 * n < s:
            return -1

        if s == 0:
            return 0

        ans = []

        for _ in range(n):
            d = min(9, s)
            ans.append(str(d))
            s -= d

        return int("".join(ans))
        
