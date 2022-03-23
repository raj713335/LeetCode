# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        dictx = {}
        
        for each in word1:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in word2:
            if each not in dictx:
                dictx[each] = -1
            else:
                dictx[each] -= 1
                
        for each in dictx.values():
            if abs(each)>3:
                return False
       
        return True
                
                
        
