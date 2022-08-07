# https://leetcode.com/problems/maximum-average-subarray-i/


import math 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        tempx = sum(nums[0: k])
        avg = tempx/k
        
        for i in range(k, len(nums)):
            tempx = (tempx-nums[i-k]+nums[i])
            avgx = tempx/k
            if avgx > avg:
                avg = avgx
                
        return avg
            
