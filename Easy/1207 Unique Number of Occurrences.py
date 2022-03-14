# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        res = {}
        
        arr_set = set(arr)
        
        for i in range(0, len(arr)):
            if arr[i] not in res:
                res[arr[i]] = 1
            else:
               res[arr[i]] += 1
        
        if len(res.values()) == len(set(res.values())):
            return True
        return False
            
        
        
