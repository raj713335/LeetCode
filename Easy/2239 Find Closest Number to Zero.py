# https://leetcode.com/problems/find-closest-number-to-zero/


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest = math.inf
        value = -math.inf
        
        for i in range(0, len(nums)):
            if abs(nums[i]) < closest:
                    closest = abs(nums[i])
                    value = nums[i]
            if abs(nums[i]) <= closest:
                if value < nums[i]:
                    closest = abs(nums[i])
                    value = nums[i]
                    
        return value
            
        
