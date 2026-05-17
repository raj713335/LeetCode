# https://leetcode.com/problems/check-adjacent-digit-differences/description/


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:

        s = str(s)

        for i in range(0, len(s)-1):
            diff = abs(int(s[i]) - int(s[i+1]))

            if diff > 2:
                return False

        return True

        
