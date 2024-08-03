# https://leetcode.com/problems/find-the-number-of-winning-players/description/

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        dictx = {}

        for player, ball in pick:
            if (player, ball) not in dictx.keys():
                dictx[(player, ball)] = 1
            else:
                dictx[(player, ball)] += 1

        count = 0
        dictx_r = {}

        for key, value in dictx.items():
            if key[0] not in dictx_r.keys():
                if value > key[0]:
                    count += 1
                    dictx_r[key[0]] = 1

        return count
        
