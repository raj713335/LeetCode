# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        prev = nums[0]
        count = 0
        
        if len(nums) == 1:
            return prev
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            else:
                if count == 0:
                    return prev
                else:
                    prev = nums[i]
                    count = 0
        
        return nums[i]
