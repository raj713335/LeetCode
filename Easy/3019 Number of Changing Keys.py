# https://leetcode.com/problems/number-of-changing-keys/description/

class Solution:
    def countKeyChanges(self, s: str) -> int:

        s = s.lower()

        count = 0

        for i in range(0, len(s)-1):
            if s[i] != s[i+1]:
                count += 1

        return count
        
