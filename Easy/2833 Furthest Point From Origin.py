# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        L = 0
        R = 0
        U = 0

        for i in range(0, len(moves)):
            if moves[i] == "L":
                L += 1
            elif moves[i] == "R":
                R += 1
            else:
                U += 1

        return (abs(L-R)+U)
