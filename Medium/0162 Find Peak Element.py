# https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        return nums.index(max(nums))
        
