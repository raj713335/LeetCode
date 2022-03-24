# https://leetcode.com/problems/sign-of-the-product-of-an-array/


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        product = 1
        
        for each in nums:
            product *= each
            
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        
