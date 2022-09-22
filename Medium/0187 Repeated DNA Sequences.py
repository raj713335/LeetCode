# https://leetcode.com/problems/repeated-dna-sequences/


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dictx = {}
        output = []
        
        for i in range(0, len(s)-9):
            if s[i:i+10] not in dictx:
                dictx[s[i:i+10]] = 0
            else:
                dictx[s[i:i+10]] = 1
                
        for key, value in dictx.items():
            if value > 0:
                output.append(key)
                
                
        return output
        
