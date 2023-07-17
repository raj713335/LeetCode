# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        sumx = 0
        length = len(nums)

        for i in range(0, length):
            if length % (i+1) == 0:
                sumx += (nums[i]**2)


        return sumx
