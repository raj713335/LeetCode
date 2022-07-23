# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        dictx = {}
        
        for i in range(lowLimit,highLimit+1):
            temp = sum(list(map(int, str(i))))
            if temp not in dictx:
                dictx[temp] = 1
            else:
                dictx[temp] += 1
                
        return max(dictx.values())
            
        
