# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        max_num = max(nums)

        # All negative case
        if max_num < 0:
            return max_num

        # Positive unique numbers only
        max_sum = sum({num for num in nums if num > 0})
        return max_sum
        
