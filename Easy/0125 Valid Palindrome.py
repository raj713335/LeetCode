# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        m = re.sub(r'[^a-z0-9]*','', s)
        
        return m[::-1]==m
        
        
        
