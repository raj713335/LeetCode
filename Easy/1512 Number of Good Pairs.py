# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    res+=1
        return res
        
