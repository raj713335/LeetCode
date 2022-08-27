# https://leetcode.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        dictx = {}
        output = []
        
        for i in range(0, len(nums)):
            if nums[i] not in dictx:
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1
   
        for key, value in dictx.items():
            if value == 1:
                output.append(key)
                
        return output
                
                
        
