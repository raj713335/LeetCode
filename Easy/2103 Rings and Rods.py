# https://leetcode.com/problems/rings-and-rods/


class Solution:
    def countPoints(self, rings: str) -> int:
        
        dictx = {}
        
        for i in range(0, len(rings), 2):
            if rings[i+1] not in dictx:
                dictx[rings[i+1]] =  [rings[i]]
            else:
                dictx[rings[i+1]].append(rings[i])

            
        count = 0
        
        for each in dictx.values():
            if len(set(each)) == 3:
                count += 1
        
        return count
        
        
        
