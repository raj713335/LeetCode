# https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:

        right = sum(nums)
        left = 0

        res = []

        for i in range(0, len(nums)):

            right -= nums[i]
            res.append(abs(right-left))
            left += nums[i]

        return res
            


