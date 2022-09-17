# https://leetcode.com/problems/subsets-ii/


from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = (())
        
        nums = sorted(nums)
        
        
        for i in range(1, len(nums)+1):
            dictx = {}
            temp = combinations(nums, i)
            output = (*output, *temp)
            
            
        output = (*output, ())   
        return set(output)
        
