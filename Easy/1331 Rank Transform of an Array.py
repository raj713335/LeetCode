# https://leetcode.com/problems/rank-transform-of-an-array/


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arrx = sorted(set(arr))
        
        rank = 1
        dictx = {}
        
        for each in arrx:
            dictx[each] = rank
            rank += 1
        
        output = []
        
        for each in arr:
            output.append(dictx[each])
            
        return output
        
