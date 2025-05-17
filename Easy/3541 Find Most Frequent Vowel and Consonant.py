# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/


from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:

        dictx_v = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        dictx_c = defaultdict(int)

        for each in s:
            if each in dictx_v:
                dictx_v[each] += 1
            else:
                dictx_c[each] += 1

        max_vowel = max(dictx_v.values()) if any(dictx_v.values()) else 0
        max_consonant = max(dictx_c.values()) if dictx_c else 0
        
        return max_vowel + max_consonant
        
