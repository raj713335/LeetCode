# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        

        index = -1
        
        for i in range(0, len(nums)):
            if i % 10 == nums[i]:
                return i
                    
        return index
        
