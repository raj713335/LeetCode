# https://leetcode.com/problems/maximum-ascending-subarray-sum/


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        sumx = nums[0]
        max_sumx = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sumx += nums[i]
            else:
                if sumx > max_sumx:
                    max_sumx = sumx
                sumx = nums[i]
                
        return max(max_sumx,sumx)
        
