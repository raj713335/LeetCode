# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/


class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        l, r = 0, 0 

        alice, bob = 0, 0 

        for r in range(0, len(colors)):
            if colors[l] != colors[r]:
                l = r
            if r - l >= 2:
                if colors[l] == "A":
                    alice += 1
                else:
                    bob += 1

        if bob >= alice:
            return False
        else:
            return True
        
