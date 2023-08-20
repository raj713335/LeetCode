# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        word = ""

        for each in words:
            word += each[0]

        if word == s:
            return True
        else:
            return False
