# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def kadane(nums):

            max_sum, curr_sum = nums[0], nums[0]

            for num in nums[1:]:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)

            return max_sum

        
        max_kadane = kadane(nums)
        
        total_sum = sum(nums)

        min_kadane = kadane([-num for num in nums])

        if total_sum == -min_kadane:
            return max_kadane

        return max(max_kadane, total_sum+min_kadane)
