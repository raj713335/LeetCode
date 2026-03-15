# https://leetcode.com/problems/count-commas-in-range/description/

class Solution:
    def countCommas(self, n: int) -> int:
        
        x = n - 999
        return x if x > 0 else 0
        
