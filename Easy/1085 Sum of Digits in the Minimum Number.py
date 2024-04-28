# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/description/

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        minx = min(nums)
        ans = 0

        for each in str(minx):
            ans += int(each)

        if ans % 2 == 0:
            return 1
        else:
            return 0
