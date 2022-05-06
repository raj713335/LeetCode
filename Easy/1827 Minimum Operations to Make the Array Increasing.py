# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        operations = 0
        
        index = nums[0]
        
        for i in range(1, len(nums)):
            if index >= nums[i]:
                operations += ((index-nums[i])+1)
                index = index + 1
            else:
                index = nums[i]
                
        return operations
        
