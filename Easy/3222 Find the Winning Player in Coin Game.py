# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        itr = 0

        while True:
            x -= 1
            y -= 4

            if x < 0 or y < 0:
                if itr % 2 == 0:
                    return "Bob"
                else:
                    return "Alice"
            
            itr += 1
        
