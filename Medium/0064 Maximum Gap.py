# https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        nums = sorted(nums)

        max_diff = 0

        for i in range(0, len(nums)-1):
            temp = nums[i+1] - nums[i]
            if temp > max_diff:
                max_diff = temp

        return max_diff
        
