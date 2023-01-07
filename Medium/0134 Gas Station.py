# https://leetcode.com/problems/gas-station/description/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = [0]
        prev = gas[0]-cost[0]
        res.append(prev)

        for i in range(1, len(gas)):
            temp = gas[i]-cost[i]+prev
            prev = temp
            res.append(prev)


        if res[-1] >= 0:
            return res.index(min(res))
        else:
            return -1

