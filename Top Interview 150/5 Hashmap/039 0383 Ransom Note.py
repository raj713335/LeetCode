class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dictx = {}
        
        for each in magazine:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                
        for each in ransomNote:
            if each not in dictx:
                return False
            elif dictx[each] < 1:
                return False
            else:
                dictx[each] -=1
            
        return True
        