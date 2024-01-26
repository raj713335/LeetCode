# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(xor, nums, k).bit_count()  
        
