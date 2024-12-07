# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        dictx = {}
        res = []
        n = len(words[0])
        total_words = n * len(words)

        for each in words:
            if each in dictx.keys():
                dictx[each] += 1
            else:
                dictx[each] = 1

        for i in range(0, len(s) - total_words + 1):
            temp_dictx = dictx.copy()
            for j in range(i, total_words + i, n):
                temp = s[j:j+n]
                if temp not in temp_dictx.keys():
                    break
                else:
                    temp_dictx[temp] -= 1

            if set(temp_dictx.values()) == {0}:
                res.append(i)

        return res



        
