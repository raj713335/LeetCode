# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/description/

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        result = 0
        
        for start in range(n):
            freq = defaultdict(int)
            valid = False
            
            for end in range(start, n):
                freq[s[end]] += 1
                
                if freq[s[end]] >= k:
                    valid = True
                
                if valid:
                    result += n - end
                    break
                    
        return result 
        
