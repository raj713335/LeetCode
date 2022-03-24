# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        val = [x**2 for x in nums]
        
        return sorted(val)
        
