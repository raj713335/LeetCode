# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        length = len(s)
        k = 1
        
        while k < length:
            if s[:k] * (length//k) == s:
                return True
            k += 1
        
        return False
        
