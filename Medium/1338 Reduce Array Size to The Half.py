# https://leetcode.com/problems/reduce-array-size-to-the-half/


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        dictx = {}
        
        for each in arr:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        

        dictx = list(dictx.items())
        
        dictx = sorted(dictx, key= lambda x: x[1], reverse = True)
        
        count = 0
        value = len(arr)
        pivot = value // 2
        
        for each in dictx:
            value -= each[1]
            if value <= pivot:
                count += 1
                return count
            else:
                count += 1
                
        
            
        
