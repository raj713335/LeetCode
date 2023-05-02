# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:


        pl1 = 1
        pl2 = 1

        score1 = 0
        score2 = 0

        count = 0

        for i in range(0, len(player1)):

            if count != 0:
                count -= 1
            else:
                pl1 = 1
            
            score1 += (pl1 * player1[i])

            if player1[i] == 10:
                pl1 = 2
                count = 2

        count = 0

        for i in range(0, len(player2)):  

            if count != 0:
                count -= 1
            else:
                pl2 = 1

            score2 += (pl2 * player2[i])

            if player2[i] == 10:
                pl2 = 2
                count = 2

        print(score1 , score2)

        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0
