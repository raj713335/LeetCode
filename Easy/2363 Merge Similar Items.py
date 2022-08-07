# https://leetcode.com/problems/merge-similar-items/


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        
        dictx = {}
        
        output = []
        
        for each in items1:
            if each[0] not in dictx:
                dictx[each[0]] = each[1]
            else:
                dictx[each[0]] += each[1]
                
        
        for each in items2:
            if each[0] not in dictx:
                dictx[each[0]] = each[1]
            else:
                dictx[each[0]] += each[1]
                
        
        for key, value in dictx.items():
            output.append([key, value])
            
            
        return sorted(output, key = lambda x : x[0])
