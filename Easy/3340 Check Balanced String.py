# https://leetcode.com/problems/check-balanced-string/description/

class Solution:
    def isBalanced(self, num: str) -> bool:

        even = 0
        odd = 0

        for i in range(0, len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])

        if even == odd:
            return True
        else:
            return False
        
