# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        left = 0
        right = sum(nums)
        count = 0
        
        for i in range(0, len(nums)-1):
            
            left += nums[i]
            right -= nums[i]
            
            
            if abs(left-right)%2 == 0:
                count += 1
                
        return count
