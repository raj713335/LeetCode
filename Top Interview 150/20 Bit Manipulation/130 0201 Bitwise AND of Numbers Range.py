# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        shift = 0
        while left < right:  # Keep shifting until both numbers become equal
            left = left >> 1
            right = right >> 1
            shift = shift + 1
        
        return left << shift  # Shift back to reconstruct the answer
