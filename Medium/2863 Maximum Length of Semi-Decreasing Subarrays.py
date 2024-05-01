# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/description/


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:

        max_length = 0
        length = len(nums)

        for i in range(0, length-1):
            for j in range(length-1, 0, -1):
                if j > i + max_length - 1:
                    if nums[i] > nums[j]:
                        max_length = j - i + 1
                        break
            if max_length > length - i + 1:
                break

        return max_length
