# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []

        I_count = 0
        D_count = len(s)

        for i in range(0, len(s)):
            if s[i] == "I":
                res.append(I_count)
                I_count += 1
            else:
                res.append(D_count)
                D_count -= 1
        res.append(I_count)
        
        return res
