# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        prev = nums[0]
        
        count = 0
        
        for i in range(1, len(nums)):
            if prev < nums[i]:
                prev = nums[i]
            else:
                count += 1

        if count == 1:
            return True

        prev = nums[-1]
        
        count = 0

        for i in range(len(nums)-2, -1, -1):
            if prev > nums[i]:
                prev = nums[i]
            else:
                count += 1

        if count > 1:
            return False
        else:
            return True

           
        
