# https://leetcode.com/problems/maximum-xor-after-operations/


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
        output = nums[0]
        
        for i in range(1, len(nums)):
            output |= nums[i]
            
        return output
        
