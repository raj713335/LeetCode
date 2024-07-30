# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        a_count = 0
        b_count = 0

        res = len(s)

        for i in range(res):
            if s[i] == "a":
                a_count += 1
        
        for i in range(res):
            if s[i] == "a":
                a_count -= 1
            
            res = min(res, a_count + b_count)

            if s[i] == "b":
                b_count += 1

        return res



        
