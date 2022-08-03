# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sumx, maxi = 0, nums[0]
        
        for num in nums:
            sumx += num
            maxi = max(sumx, maxi)
            if (sumx < 0):
                sumx = 0
                
        return maxi
        
