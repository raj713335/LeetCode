# https://leetcode.com/problems/unique-middle-element/description/

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        n = len(nums)//2

        return nums.count(nums[n]) == 1 
        
