# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        dictx = { 'a' : 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1 }
        
        left, right = 0, 0
        
        for i in range(0, len(s)//2):
            if s[i] in dictx:
                left += 1
                
        for j in range(len(s)//2, len(s)):
            if s[j] in dictx:
                right += 1
                
        if left == right:
            return True
        else:
            return False
                
        
