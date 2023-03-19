# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        dictx = {"a": 1, "e": 1, "i": 1, "o":1, "u": 1}

        count = 0

        for i in range(left, right+1):
            if words[i][0] in dictx:
                if words[i][-1] in dictx:
                    count += 1

        return count
