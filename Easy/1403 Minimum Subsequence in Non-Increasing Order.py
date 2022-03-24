# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        nums = sorted(nums)
        
        left = sum(nums)
        right = 0
        
        for i in range(len(nums)-1,-1,-1):
            if left<right:
                return nums[i+1:][::-1]
            else:
                left -= nums[i]
                right += nums[i]
                
        return nums
            
        
        
