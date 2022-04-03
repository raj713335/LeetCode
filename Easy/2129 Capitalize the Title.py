# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split(" ")
        
        for i in range(0, len(s)):
            if len(s[i]) > 2:
                s[i] = s[i].capitalize()
            else:
                s[i] = s[i].lower()
            
        return " ".join(s)
            
        
