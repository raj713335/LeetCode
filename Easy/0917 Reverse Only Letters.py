# https://leetcode.com/problems/reverse-only-letters/


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        listx = []
        
        ss = list(s)
        
        for i in range(0, len(s)):
            if s[i].isalpha():
                listx.append(s[i])
                

        
        for i in range(0, len(s)):
            if s[i].isalpha():
                temp = listx.pop()
                ss[i] = temp
        
        return "".join(ss)
                
            
        
