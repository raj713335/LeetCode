# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        
        max_count = 1
        
        count = 1
        
        last = s[0]
        
        for i in range(1, len(s)):
            if s[i] == last:
                count+=1
                if max_count < count:
                    max_count = count
            else:
                last = s[i]
                count = 1
                
        return max_count
                    
        
