# https://leetcode.com/problems/confusing-number/description/

class Solution:
    def confusingNumber(self, n: int) -> bool:

        mapx = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        ans = ""

        for each in str(n):
            if each not in mapx:
                return False
            else:
                ans += mapx[each]

        if ans[::-1] != str(n):
            return True
        else:
            return False
        
