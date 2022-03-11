# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = []
        
        s = s.split(" ")
        
        for each in s:
            res.append(each[::-1])
            
        return " ".join(res)
        
