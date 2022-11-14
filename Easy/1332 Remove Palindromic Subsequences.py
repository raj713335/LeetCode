# https://leetcode.com/problems/remove-palindromic-subsequences/description/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
        
