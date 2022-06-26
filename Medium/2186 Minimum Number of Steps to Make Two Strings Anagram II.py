# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dictx = {}
        sumx = 0
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] +=1
        for each in t:
            if each not in dictx:
                dictx[each] = -1
            else:
                dictx[each] -= 1
                
        for each in dictx.values():
            sumx+= abs(each)
        return sumx
