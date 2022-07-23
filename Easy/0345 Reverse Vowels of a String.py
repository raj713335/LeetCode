# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        listx = []
        
        
        for each in s:
            if each == "a" or each == "e" or each == "i" or each == "o" or each == "u" or each == "A" or each == "E" or each == "I" or each == "O" or each == "U":
                listx.append(each)
                
        
        s = list(s)
        
        for i in range(0, len(s)):
            each = s[i]
            if each == "a" or each == "e" or each == "i" or each == "o" or each == "u" or each == "A" or each == "E" or each == "I" or each == "O" or each == "U":
                temp = listx.pop()
                s[i] = temp
                
        return "".join(s)
            
        
