# https://leetcode.com/problems/relative-sort-array/


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        dictx = {}
        output = []
        temp = []
        
        for each in arr2:
            dictx[each] = 0
            
            
        for each in arr1:
            if each in dictx:
                dictx[each] += 1
            else:
                temp.append(each)
            
        for key, value in dictx.items():
            output.extend([key] * value)
            
            
        return output + sorted(temp)
            
        
        
