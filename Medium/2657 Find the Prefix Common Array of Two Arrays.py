# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        dictx = {}

        res = []

        for i in range(0, len(A)):
            if A[i] not in dictx.keys():
                dictx[A[i]] = 1
            else:
                dictx[A[i]] += 1

            if B[i] not in dictx.keys():
                dictx[B[i]] = 1
            else:
                dictx[B[i]] += 1
            
            count = 0

            for each in dictx.values():
                if each == 2:
                    count += 1

            res.append(count)

        return res
