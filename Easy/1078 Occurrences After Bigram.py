# https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        res = []
        
        
        text = text.split(" ")
        
        for i in range(0, len(text)-3+1):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
                
        return res
        
