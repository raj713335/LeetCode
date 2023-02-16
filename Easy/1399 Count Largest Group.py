# https://leetcode.com/problems/count-largest-group/


class Solution:
    def countLargestGroup(self, n: int) -> int:

        dictx = {}

        for i in range(1, n+1):
            temp = 0
            for each in str(i):
                temp += int(each)
            if temp not in dictx:
                dictx[temp] = [i]
            else:
                dictx[temp].append(i)


        key_dictx = {}

        for key, value in dictx.items():
            val = len(value)

            if val not in key_dictx:
                key_dictx[val] = 1
            else:
                key_dictx[val] += 1

        return key_dictx[max(list(key_dictx.keys()))]
