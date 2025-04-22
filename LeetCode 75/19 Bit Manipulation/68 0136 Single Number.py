# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0

        for num in nums:
            res = res ^ num

        return res
