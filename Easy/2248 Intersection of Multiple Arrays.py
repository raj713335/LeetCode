# https://leetcode.com/problems/intersection-of-multiple-arrays/


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        dictx = {}
        
        for each in nums[0]:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        for each in nums[1:]:
            temp_dictx = {}
            for val in each:
                if val in dictx:
                    if val not in temp_dictx:
                        temp_dictx[val] = 1
                    else:
                        temp_dictx[val] += 1
                        
            dictx = temp_dictx
            
        return(sorted(list(dictx.keys())))
