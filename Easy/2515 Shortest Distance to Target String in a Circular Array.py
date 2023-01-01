# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/


import math

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        index = []
        shortest_index = math.inf

        length = len(words)

        for i in range(0, len(words)):
            if words[i] == target:
                index.append(i)

        for each in index:
            temp = min(abs(startIndex-each), (startIndex+(length-each)), (each+(length-startIndex)))
            if temp < shortest_index:
                shortest_index = temp

        print(shortest_index)

        if shortest_index == math.inf:
            return -1

        return int(shortest_index)
