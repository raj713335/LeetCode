# https://leetcode.com/problems/find-the-town-judge/description/


class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        dictx = {}

        setx = {}

        if trust == []:

            if n == 1:

                return 1

            if n == 2:

                return -1

        for each in trust:

            setx[each[0]] = 1

            if each[1] not in dictx:

                dictx[each[1]] = [each[0]]

            else:

                dictx[each[1]].append([each[0]])

        for key, value in dictx.items():

            if len(value) == n-1:

                if key not in setx:

                    return key

        return -1
