# https://leetcode.com/problems/minimum-queen-moves-to-reach-target/description/


class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:

        temp = abs(source[0] - target[0])

        if source == target:
            return 0

        elif source[0] == target[0]:
            return 1

        elif source[1] == target[1]:
            return 1

        elif (source[0] + temp == target[0] or source[0] - temp == target[0]) and (source[1] + temp == target[1] or source[1] - temp == target[1]):
            return 1 

        else:
            return 2
        
