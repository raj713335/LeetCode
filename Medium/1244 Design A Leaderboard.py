# https://leetcode.com/problems/design-a-leaderboard/description/


class Leaderboard:

    def __init__(self):
        self.dictx = {}
        

    def addScore(self, playerId: int, score: int) -> None:

        if playerId not in self.dictx:
            self.dictx[playerId] = score
        else:
            self.dictx[playerId] += score
        

    def top(self, K: int) -> int:

        listx = sorted(self.dictx.values(), reverse=True)

        return sum(listx[:K])
        

    def reset(self, playerId: int) -> None:
        del self.dictx[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
