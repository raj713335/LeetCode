# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if nums == sorted(nums):
            return True
        elif nums == sorted(nums, reverse=True):
            return True
        return False
        
