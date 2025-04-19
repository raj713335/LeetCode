# https://leetcode.com/problems/move-zeroes/description/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] == 0:
                nums.append(nums[i])
                nums.remove(nums[i])
            i += 1   