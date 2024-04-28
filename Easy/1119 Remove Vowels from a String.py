# https://leetcode.com/problems/remove-vowels-from-a-string/description/

class Solution:
    def removeVowels(self, s: str) -> str:

        listx = []

        for i in range(0, len(s)):
            if s[i] not in "aeiou":
                listx.append(s[i])

        return "".join(listx)
        
