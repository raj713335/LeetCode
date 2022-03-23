# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        dictx = {"b":0, "a":0, "l":0, "o":0, "n":0}
        
        for each in text:
            if each in dictx:
                dictx[each] -= 1
                
        dictx["l"] = -(abs(dictx["l"]) // 2)
        dictx["o"] = -(abs(dictx["o"]) // 2)
                
        return abs(max(dictx.values()))
        
