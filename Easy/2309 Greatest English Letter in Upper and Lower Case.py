# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/


class Solution:
    def greatestLetter(self, s: str) -> str:
        
        dictx = {}
        
        for each in s:
            dictx[each] = 1

        while len(dictx) > 1:
            keys = max(dictx.keys())
            if keys.lower() in dictx and keys.upper() in dictx:
                return keys.upper()
            else:
                del dictx[keys]
                
        return ""
        
