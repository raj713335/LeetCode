# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:


        count = 0

        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]):
                    lengthx = len(words[i])
                    if words[j][0: lengthx] == words[i] and words[j][-lengthx:] == words[i]:
                        count += 1

        return count
        
