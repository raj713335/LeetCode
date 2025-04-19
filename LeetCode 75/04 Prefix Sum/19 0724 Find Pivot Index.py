# https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pivot = -1

        left = 0
        right = sum(nums)

        for i in range(0, len(nums)):
            right -= nums[i]

            if left == right:
                return i

            left += nums[i]

        return pivot
