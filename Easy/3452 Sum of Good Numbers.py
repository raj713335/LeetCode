# https://leetcode.com/problems/sum-of-good-numbers/description/

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
        sumx = 0
        
        for i in range(0, len(nums)):
            a, b = False, False
            index_low = i - k
            index_high = i + k
            
            if index_low < 0:
                a = True
            elif nums[i] > nums[index_low]:
                a = True
                
            if index_high >= n:
                b = True
            elif nums[i] > nums[index_high]:
                b = True
                
            if a and b:
                sumx += nums[i]
                
        return sumx
        
