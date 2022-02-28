# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_val = 0
        
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                res = (nums[i]-1)*(nums[j]-1)
                if max_val < res:
                    max_val = res
                    
        return max_val
        
