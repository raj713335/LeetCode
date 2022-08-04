# https://leetcode.com/problems/maximum-difference-between-increasing-elements/


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        diff = -1
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    temp = nums[j] - nums[i]
                    if temp > diff:
                        diff = temp
                    
        return diff
                
        
