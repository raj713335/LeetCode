# https://leetcode.com/problems/faulty-keyboard/description/

class Solution:
    def finalString(self, s: str) -> str:

        output = ""

        for i in range(0, len(s)):
            if s[i] == "i":
                output = output[::-1]
            else:
                output += s[i]
        
        return output
