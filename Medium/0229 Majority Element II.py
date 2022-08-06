# https://leetcode.com/problems/majority-element-ii/


import math 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        dictx = {}
        
        output = []
        
        maj_rank = len(nums)//3
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
                

        
        for key, val in dictx.items():
            if val > maj_rank:
                output.append(key)
                
        return output
        
