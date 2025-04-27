# https://leetcode.com/problems/count-number-of-texts/description/

MOD = 10**9 + 7

class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        memo = {}
        def dp(i):
            if (i == 0):
                return 1
            if i in memo:
                return memo[i]
            res = dp(i - 1)
            if i - 2 >= 0 and pressedKeys[i - 2] == pressedKeys[i - 1]:
                res += dp(i - 2)
                if i - 3 >= 0 and pressedKeys[i-3] == pressedKeys[i - 1]:
                    res += dp(i - 3)
                    if i - 4 >= 0 and pressedKeys[i-4] == pressedKeys[i - 1] and pressedKeys[i - 1] in "79":
                        res += dp(i - 4)
            memo[i] = res % (10 ** 9 + 7)
            return memo[i]
        return dp(len(pressedKeys)) % (10 ** 9 + 7)
        
