# https://leetcode.com/problems/naming-a-company/description/



class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        wordMap = collections.defaultdict(set)
        for w in ideas:
            wordMap[w[0]].add(w[1:])
        
        res = 0


        for char1 in wordMap:
            for char2 in wordMap:
                if char1 == char2:
                    continue
                intersect = 0
                for w in wordMap[char1]:
                    if w in wordMap[char2]:
                        intersect += 1

                distinct1 = len(wordMap[char1]) - intersect
                distinct2 = len(wordMap[char2]) - intersect

                res += distinct1 * distinct2

        return res
