# https://leetcode.com/problems/largest-number-at-least-twice-of-others/


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        numsx = sorted(nums)
        
        if numsx[-1] >= 2*numsx[-2]:
            return nums.index(numsx[-1])
        return -1
        
