# https://leetcode.com/problems/shortest-word-distance-iii/description/


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        dictx = {}

        for i in range(0, len(wordsDict)):
            if wordsDict[i] not in dictx:
                dictx[wordsDict[i]] = [i]
            else:
                dictx[wordsDict[i]].append(i)

        min_distnce = math.inf

        if word1 == word2:
            listx = dictx[word1]

            for i in range(0, len(listx)):
                for j in range(i+1, len(listx)):
                    val = abs(listx[i]-listx[j])
                    if val < min_distnce:
                        min_distnce = val
                        if min_distnce == 1:
                            return 1
        else:
            for i in dictx[word1][::-1]:
                for j in dictx[word2][::-1]:
                    val = abs(i-j)
                    if val < min_distnce:
                        min_distnce = val
                        if min_distnce == 1:
                            return 1

        return min_distnce
        
