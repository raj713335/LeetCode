# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


class Solution:
    def minLength(self, s: str) -> int:
        
        flag = True

        while flag:
            flag = False
            if "AB" in s:
                s = s.replace("AB", "")
                flag = True
            
            if "CD" in s:
                s = s.replace("CD", "")
                flag = True

        return len(s)

            
