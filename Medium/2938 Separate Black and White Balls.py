# https://leetcode.com/problems/separate-black-and-white-balls/description/?envType=daily-question&envId=2024-10-15


class Solution:
    def minimumSteps(self, s: str) -> int:

        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] == "0":
                res += (r-l)
                l += 1

        return res
        
