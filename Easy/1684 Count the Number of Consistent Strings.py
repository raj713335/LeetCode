# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        dictx = {}
        
        for each in allowed:
            dictx[each] = 1
            
        count = 0
        
        for each in words:
            flag = True
            for i in range(0, len(each)):
                if each[i] not in dictx:
                    flag = False
                    break
            if flag:
                count += 1
        return count
        
