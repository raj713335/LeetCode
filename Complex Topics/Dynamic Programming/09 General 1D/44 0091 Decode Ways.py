# https://leetcode.com/problems/decode-ways/description/


class Solution:
    def numDecodings(self, s: str) -> int:

        dictx = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        dp = {}

        n = len(s)

        def dfs(index):

            if index == n:
                return 1
            
            if s[index] == '0':
                return 0

            if index in dp:
                return dp[index]

            option_1 = dfs(index + 1)
            
            option_2 = 0
            if index + 1 < n and 10 <= int(s[index:index+2]) <= 26:
                option_2 = dfs(index + 2)
            
            dp[index] = option_1 + option_2
            return dp[index]

        return dfs(0)

        
