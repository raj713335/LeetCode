# https://leetcode.com/problems/find-the-pivot-integer/description/


class Solution:
    def pivotInteger(self, n: int) -> int:

        nums = [x for x in range(1, n+1)]

        for i in range(0, len(nums)):
            if sum(nums[:i+1]) == sum(nums[i:]):
                return i+1

        return -1
