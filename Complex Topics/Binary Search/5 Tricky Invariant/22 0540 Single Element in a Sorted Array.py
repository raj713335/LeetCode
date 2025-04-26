# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]

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
