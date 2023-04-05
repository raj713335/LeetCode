# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        maxi = 0

        for i in range(0, len(s)):
            zero = 0
            one = 0

            while (i < len(s) and s[i] == "0"):
                zero += 1
                i += 1

            while (i < len(s) and s[i] == "1"):
                one += 1
                i += 1

            length = min(zero, one) * 2

            maxi = max(length, maxi)

        
        return maxi

            
