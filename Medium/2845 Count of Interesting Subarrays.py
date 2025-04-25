# https://leetcode.com/problems/count-of-interesting-subarrays/description/

from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:


        countMap = defaultdict(int)
        countMap[0] = 1  # To handle when the prefix itself is interesting
        
        prefix = 0
        res = 0
        
        for num in nums:
            if num % modulo == k:
                prefix += 1
            
            mod_val = prefix % modulo
            target = (mod_val - k + modulo) % modulo
            
            res += countMap[target]
            countMap[mod_val] += 1
        
        return res
        
