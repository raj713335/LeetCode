# https://leetcode.com/problems/split-strings-by-separator/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        words_new = []

        for i in range(0, len(words)):
            for each in words[i].split(separator):
                if each != "":
                    words_new.append(each)

        return words_new
