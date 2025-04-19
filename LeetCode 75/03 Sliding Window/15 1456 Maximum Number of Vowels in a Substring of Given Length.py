# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_substring = 0

        dictx = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        sub = s[0:k]
        temp = 0
        for each in sub:
            if each in dictx:
                temp += 1

        if temp > max_substring:
            max_substring = temp

        for i in range(k, len(s)):

            if sub[0] in dictx:
                temp -= 1

            sub = sub[1:] + s[i]

            if s[i] in dictx:
                temp += 1

            if temp > max_substring:
                max_substring = temp

        return max_substring
