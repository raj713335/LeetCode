# https://leetcode.com/problems/verifying-an-alien-dictionary/description/


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dictx = {}

        for i in range(0, len(order)):
            dictx[order[i]] = i


        for i in range(1, len(words)):
            for j in range(0, len(words[i-1])):
                try:
                    if words[i-1][j] != words[i][j]:
                        if dictx[words[i-1][j]] > dictx[words[i][j]]:
                            return False
                        else:
                            break
                except:
                    return False


        return True
