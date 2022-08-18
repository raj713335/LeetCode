# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        count = len(nums)
        
        for each in nums:
            if each == 0:
                count -= 1
                
        return count
        
