# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i

        return len(nums)
        
