# https://leetcode.com/problems/sort-vowels-in-a-string/description/

class Solution:
    def sortVowels(self, s: str) -> str:

        s = list(s)

        vowels = { "A" : 0, "E" : 0, "I" : 0, "O" : 0, "U" : 0, "a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0 }
        
        vowels_value = []

        for i in range(0, len(s)):
            if s[i] in vowels:
                vowels_value.append(s[i])

        vowels_value = sorted(vowels_value)

        count = 0
        for i in range(0, len(s)):
            if s[i] in vowels:
                s[i] = vowels_value[count]
                count += 1

        return "".join(s)
