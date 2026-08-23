# https://leetcode.com/problems/check-ascii-palindromic/description/

class Solution:
    def isPalindromic(self, s: str) -> bool:

        res = ""

        for char in s:
            number = ord(char)
            binary_string = f"{number:08b}"
            res += binary_string

        return res == res[::-1]

