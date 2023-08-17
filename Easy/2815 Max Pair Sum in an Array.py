# https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        max_sum = -1

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if max(list(str(nums[i]))) == max(list(str(nums[j]))):
                    temp = nums[i] + nums[j]
                    if temp > max_sum:
                        max_sum = temp

        return max_sum
