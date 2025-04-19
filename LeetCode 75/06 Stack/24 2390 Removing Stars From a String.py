# https://leetcode.com/problems/removing-stars-from-a-string/description/


class Solution:
    def removeStars(self, s: str) -> str:
        
        res = []
        for c in s:
            if c != '*':
                res.append(c)
            elif res:
                res.pop()
                
        return ''.join(res)
                
            
        