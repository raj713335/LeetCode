# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: x[1])

        length = 1

        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if end < pairs[i][0]:
                length += 1
                end = pairs[i][1]

        return length
