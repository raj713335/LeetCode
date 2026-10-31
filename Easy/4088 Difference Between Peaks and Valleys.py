# https://leetcode.com/problems/difference-between-peaks-and-valleys/description/

class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:


        peak = 0
        vally = 0

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                peak += nums[i]
            elif nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                vally += nums[i]


        return peak - vally 
        
