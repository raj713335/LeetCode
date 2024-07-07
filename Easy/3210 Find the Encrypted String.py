# https://leetcode.com/problems/find-the-encrypted-string/description/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        n = k % len(s)

        s = s[n:] + s[:n]

        return s
        
