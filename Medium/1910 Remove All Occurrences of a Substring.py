# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while(part in s):
            s = s.replace(part,"",1)
        return s
        
