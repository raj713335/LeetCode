# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


class Solution:
    def check(self, nums: List[int]) -> bool:
        
        
        
        minx = min(nums) 
        countx = nums.count(minx)
        nums_sorted = sorted(nums)
        
        while countx > 0:
            nums[:] = nums[nums.index(minx):]+nums[0:nums.index(minx)]
            if nums_sorted == nums:
                return True
            countx -= 1
        
            nums[:] =  nums[1:]+[nums[0]]
            
        return False
                
        
