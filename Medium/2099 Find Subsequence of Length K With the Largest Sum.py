# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/


import math
from itertools import permutations 

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        values = []
        
        for i in range(0, len(nums)):
            values.append([nums[i], i])
            
        values = sorted(values, key = lambda x : x[0])
        
        values = sorted(values[-k:], key = lambda x : x[1])
        
        output = []
        
        for each in values:
            output.append(each[0])
            
        return output
        
        
        
