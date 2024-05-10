# https://leetcode.com/problems/shortest-word-distance-ii/description/


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dictx = {}

        for i in range(0, len(wordsDict)):
            if wordsDict[i] not in self.dictx:
                self.dictx[wordsDict[i]] = [i]
            else:
                self.dictx[wordsDict[i]].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:

        min_distnce = math.inf

        for i in self.dictx[word1]:
            for j in self.dictx[word2]:
                val = abs(i-j)
                if val < min_distnce:
                    min_distnce = val

        return min_distnce

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
