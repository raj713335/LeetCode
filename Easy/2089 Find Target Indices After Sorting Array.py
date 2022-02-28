# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        nums = sorted(nums)
        
        for i in range(0, len(nums)):
            if nums[i] == target:
                res.append(i)
                
        return res
        
