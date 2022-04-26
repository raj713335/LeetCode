# https://leetcode.com/problems/find-triangular-sum-of-an-array/


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        
        while(len(nums)!=1):
            temp_array = []
            for i in range(0, len(nums)-1):
                temp_array.append((nums[i]+nums[i+1])%10)
            nums = temp_array
        return nums[0]
            
        
