# https://leetcode.com/problems/compute-alternating-sum/description/

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        odd = 0
        even = 0

        for i in range(0, len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]

        return even - odd
        
