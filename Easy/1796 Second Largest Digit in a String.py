# https://leetcode.com/problems/second-largest-digit-in-a-string/


class Solution:
    def secondHighest(self, s: str) -> int:
        
        dictx = {}
        
        for each in s:
            try:
                dictx[int(each)] = 1
            except: 
                pass
            
        try:
            return sorted(dictx.keys())[-2]
        except:
            return -1
        
