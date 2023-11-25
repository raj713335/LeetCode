# https://leetcode.com/problems/find-words-containing-character/description/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        res = []

        for i in range(0, len(words)):
            for k in range(0, len(words[i])):
                if words[i][k] == x:
                    res.append(i)
                    break

        return res
        
