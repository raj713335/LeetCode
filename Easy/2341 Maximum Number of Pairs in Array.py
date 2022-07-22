# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        set_nums = set(nums)
        
        left = 0
        pair = 0
        
        for each in set_nums:
            temp = nums.count(each)
            if temp%2 == 0:
                pair += temp//2
            else:
                pair += temp //2
                left += 1
                
        return [pair, left]
            
        
