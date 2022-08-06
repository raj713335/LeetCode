# https://leetcode.com/problems/array-partition/


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        sumx = 0
        
        for i in range(0, len(nums), 2):
            sumx += nums[i]
            
        return sumx
        
