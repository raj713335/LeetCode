# https://leetcode.com/problems/minimum-total-operations/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
        return count
        
