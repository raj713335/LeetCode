# https://leetcode.com/problems/merge-strings-alternately/description/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1 = len(word1)
        len2 = len(word2)

        i, j = 0, 0

        res = ""

        while i < len1 or j < len2:
            
            if i < len1:
                res += word1[i]
                i += 1

            if j < len2:
                res += word2[j]
                j += 1

        return res

        