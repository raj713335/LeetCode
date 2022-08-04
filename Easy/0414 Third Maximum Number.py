# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = sorted(set(nums))
        
        if len(nums) > 2:
            return nums[-3]
        else:
            return nums[-1]
        
