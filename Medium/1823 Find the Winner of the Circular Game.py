# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = [x for x in range(1, n+1)]

        i = 0

        while n > 1:
            i += (k-1)
            if i >= n:
                i = i % n
            del players[i]
            n -= 1

        return players[0]
        
