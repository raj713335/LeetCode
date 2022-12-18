# https://leetcode.com/problems/count-pairs-of-similar-strings/description/



class Solution:
    def similarPairs(self, words: List[str]) -> int:

        dictx = {}
        count = 0

        for each in words:
            value = sorted(set(each))
            key = len(value)
            if key in dictx:
                dictx[key].append(value)
            else:
                dictx[key] = [value]

        for key, value in dictx.items():
            for i in range(0, len(value)-1):
                for j in range(i+1, len(value)):
                    if value[i] == value[j]:
                        count += 1


        return count

