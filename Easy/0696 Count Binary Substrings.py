# https://leetcode.com/problems/count-binary-substrings/description/

from itertools import combinations

class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))
        
        
