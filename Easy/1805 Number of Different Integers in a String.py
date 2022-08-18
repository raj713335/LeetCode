# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        dictx = {}
        
        temp = ""
        for each in word:
            if each.isnumeric():
                temp += each
            else:
                if temp != "":
                    dictx[int(temp)] = 1
                temp = ""
        if temp != "":
            dictx[int(temp)] = 1      
        return len(dictx)                
        
