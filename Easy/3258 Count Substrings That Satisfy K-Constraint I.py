# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        count = 0

        x = s.count("1")
        y = s.count("0")

        if x <= k or y <= k:
            count += 1

        for i in range(1, len(s)):
            for j in range(0, len(s)-i+1):
                temp = s[j:j+i]
                x = temp.count("1")
                y = temp.count("0")

                if x <= k or y <= k:
                    count += 1

        return count
        
