# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i]> nums[j]:
                    count += 1
            res.append(count)
            
        return res
                    
        
