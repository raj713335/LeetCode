# https://leetcode.com/problems/find-special-substring-of-length-k/description/


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        for i in range(0, len(s)-k+1):
            if len(set(s[i:i+k])) == 1:
                if i - 1 >= 0:
                    if s[i-1] == s[i]:
                        continue
                if i + k < len(s):
                    if s[i+k] == s[i]:
                        continue
                return True

        return False
        
