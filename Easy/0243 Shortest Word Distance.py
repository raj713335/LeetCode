# https://leetcode.com/problems/shortest-word-distance/description/

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        a = []
        b = []

        for i in range(0, len(wordsDict)):
            if wordsDict[i] == word1:
                a.append(i)
            
            if wordsDict[i] == word2:
                b.append(i)

        minx = len(wordsDict)

        for i in range(0, len(a)):
            for j in range(0, len(b)):
                temp = abs(a[i]-b[j])
                if temp < minx:
                    minx = temp

        return minx
        
