# https://leetcode.com/problems/regular-expression-matching/

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        p = re.compile(p)
        try:
            ss= (re.match(p, s)).group()
        except:
            return False
       
        if ss == s:
            return True
        else:
            return False
