# https://leetcode.com/problems/continuous-subarray-sum/



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder = {0: -1} 
        total = 0
        
        for i, val in enumerate(nums):
            total += val
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
            
        return False
