# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        dictx = {}
        count = 0

        for each in tasks:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        for key, val in dictx.items():
            rem = val % 3
            div = val // 3

            if div == 0 and rem < 2:
                return -1
            elif rem == 0:
                count += div
            else:
                count += (div+1)

        return count 
        
