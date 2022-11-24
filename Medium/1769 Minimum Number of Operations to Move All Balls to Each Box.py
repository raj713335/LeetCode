# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        dictx = []
        output = []

        for i in range(0, len(boxes)):
            if boxes[i] == "1":
                dictx.append(i)


        for i in range(0, len(boxes)):
            val = 0
            for each in dictx:
                val += abs(i-each)
            output.append(val)

        return output
