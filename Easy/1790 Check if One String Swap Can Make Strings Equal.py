# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        dictx = []
        
        count = 0
        
        
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                dictx.append([s1[i], s2[i]])
                count += 1
                if count > 2:
                    return False
                
        if count == 0:
            return True
        elif count == 1:
            return False
        if dictx[0][0] == dictx[1][1] and dictx[0][1] == dictx[1][0]:
            return True
        else:
            return False
            
