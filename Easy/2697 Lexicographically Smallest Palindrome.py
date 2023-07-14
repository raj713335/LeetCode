# https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        lenx = len(s)

        s = list(s)

        for i in range(0, lenx//2):
            s[i] = s[lenx-i-1] = min(s[i], s[lenx-i-1])

        return "".join(s)
