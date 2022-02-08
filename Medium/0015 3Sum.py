# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        nums = sorted(nums)
        
        for k in range(0, len(nums)):
            target = -(nums[k])
            l, r = k+1, len(nums)-1
            while(l<r):
                sum_two = nums[l]+nums[r]
                if sum_two < target:
                    l += 1
                elif sum_two > target:
                    r -= 1
                else:
                    res.add((nums[k],nums[l],nums[r]))
                    l += 1
                    r -= 1
                    
        return res
            
            
        
        
