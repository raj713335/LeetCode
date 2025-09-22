# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/description/

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:

        bitwise_or = 0

        for num in nums:
            if num % 2 == 0:
                bitwise_or = bitwise_or | num

        return bitwise_or
        
