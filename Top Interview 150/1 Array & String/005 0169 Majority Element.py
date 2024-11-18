# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority_mark = len(nums)//2
        
        for each in set(nums):
            if nums.count(each) > majority_mark:
                return each
        
