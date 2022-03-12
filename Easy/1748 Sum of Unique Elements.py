# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        sumx = 0
        
        nums_unique = set(nums)
        
        for each in nums_unique:
            if nums.count(each) == 1:
                sumx += each
                
        return sumx
        
