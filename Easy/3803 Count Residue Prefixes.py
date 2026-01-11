# https://leetcode.com/problems/count-residue-prefixes/description/

class Solution:
    def residuePrefixes(self, s: str) -> int:

        result = 0
        
        for index in range(len(s)):

            prefix = s[:index + 1]

            if len(set(prefix)) == len(prefix) % 3:
                
                result = result + 1

        return result
        
