# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lenx = len(needle)
        
        if lenx == 0:
            return 0
        
        for i in range(0, len(haystack)):
            if haystack[i:i+lenx] == needle:
                return i
            
        return -1
