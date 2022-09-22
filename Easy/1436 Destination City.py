# https://leetcode.com/problems/destination-city/


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        dictx = {}
        
        for city in paths:
            if city[0] not in dictx:
                dictx[city[0]] = city[1]
        
        val = paths[0][0]
        
        while True:
            
            try:
                val = dictx[val]
            except:
                return val
            
            
        
