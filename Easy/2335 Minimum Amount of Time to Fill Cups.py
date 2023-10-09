# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

class Solution:
    def fillCups(self, amount: List[int]) -> int:

        return max(max(amount), ceil(sum(amount)/2))
        
