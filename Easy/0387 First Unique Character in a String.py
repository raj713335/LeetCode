# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(0, len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
        
