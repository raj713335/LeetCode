# https://leetcode.com/problems/armstrong-number/description/

class Solution:
    def isArmstrong(self, n: int) -> bool:

        length = len(str(n))
        n = str(n)
        ans = 0
        
        for i in range(0, length):
            ans += int(n[i]) ** length

        if ans == int(n):
            return True
        else:
            return False
        
