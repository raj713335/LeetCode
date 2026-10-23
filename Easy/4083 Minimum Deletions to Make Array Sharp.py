# https://leetcode.com/problems/minimum-deletions-to-make-array-sharp/

class Solution:
    def minDeletions(self, nums: list[int]) -> int:

        count = 0

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1

        
        return count
        
