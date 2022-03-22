# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x, y = 0, 0

        for move in moves:
            if move == "U":
                x += 1
            elif move == "D":
                x -= 1
            elif move == "L":
                y -= 1
            elif move == "R":
                y += 1
        if x == 0 and y ==0:
            return True
        else:
            return False
        
