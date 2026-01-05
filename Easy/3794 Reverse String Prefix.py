# https://leetcode.com/problems/reverse-string-prefix/description/

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        return s[:k][::-1] + s[k:]
        
