# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        
        flag = True
        
        for i in range(0, len(s)):
            if s[i] == 'b':
                flag = False
            
            if s[i] == 'a':
                if flag == False:
                    return False
                
        return True
            
            
        
