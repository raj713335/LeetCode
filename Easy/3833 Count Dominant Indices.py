# https://leetcode.com/problems/count-dominant-indices/description/

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        count = 0

        n = len(nums)
        value = sum(nums)

        for i in range(0, len(nums)-1):
            n = n - 1
            value = value - nums[i]

            if nums[i] > (value/n):
                count += 1

        return count
        

