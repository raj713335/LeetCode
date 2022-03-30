# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(0, len(s)-2):
            if len(set(s[i:i+3])) == 3:
                count += 1
                
        return count
        
