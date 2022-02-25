# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        dictx = {}
        res = ""
        
        for i in range(0, len(s)):
            dictx[indices[i]] = s[i]
            
            
        for i in range(0, len(s)):
            res += dictx[i]
            
        return res
            
