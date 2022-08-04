# https://leetcode.com/problems/maximum-score-after-splitting-a-string/


class Solution:
    def maxScore(self, s: str) -> int:
        
        max_score = 0
        
        for i in range(1, len(s)):
            
            temp = str(s[:i]).count("0") + str(s[i:]).count("1")
            #print( str(s[:i]) , str(s[i:]), temp)
            
            if temp > max_score:
                max_score = temp
                
        return max_score
            
        
