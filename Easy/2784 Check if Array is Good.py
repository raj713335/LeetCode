# https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:

        val = []

        for i in range(1, len(nums)):
            val.append(i)
        val.append(len(nums)-1)

        if sorted(nums) == val:
            return True
        return False
