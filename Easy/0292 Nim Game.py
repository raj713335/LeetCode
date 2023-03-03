# https://leetcode.com/problems/nim-game/description/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        
