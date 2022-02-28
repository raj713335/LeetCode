class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        
        lenx = len(needle)
        
        if lenx == 0:
            return 0
        
        for i in range(0, len(haystack)):
            if haystack[i:i+lenx] == needle:
                return i
            
        return -1
        
