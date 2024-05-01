# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        count = 0
        for i in range(0, len(s)-k+1):
            if len(set(s[i:i+k])) == k:
                count += 1

        return count
        
