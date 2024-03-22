# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        reverse = s[::-1]

        for i in range(0, len(s)-1):
            for j in range(0, len(reverse)-1):
                if s[i:i+2] == reverse[j:j+2]:
                    return True
        
        return False
        
