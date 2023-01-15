# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        element_sum = sum(nums)
        digit_sum = 0

        for each in nums:
            for i in str(each):
                digit_sum += int(i)


        return abs(element_sum-digit_sum)
