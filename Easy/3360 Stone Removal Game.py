# https://leetcode.com/problems/stone-removal-game/description/


class Solution:
    def canAliceWin(self, n: int) -> bool:

        flag = True

        stones = 10

        while n >= stones:
            n -= stones
            stones -= 1
            if flag:
                flag = False
            else:
                flag = True

        
        if flag:
            return False
        else:
            return True

        
        
