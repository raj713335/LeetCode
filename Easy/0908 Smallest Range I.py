# https://leetcode.com/problems/smallest-range-i/


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        a = max(nums)
        b = min(nums)
        
        if b+k>a-k:
            return 0
        else:
            return (a-k)-(b+k)
        
        
        
        
