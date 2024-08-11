# https://leetcode.com/problems/snake-in-matrix/description/

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        matrix = []
        counter = 0

        for i in range(n):
            sub_matrix = []
            for j in range(n):
                sub_matrix.append(counter)
                counter += 1
            matrix.append(sub_matrix)

        i, j = 0, 0

        for cmd in commands:
            if cmd == "DOWN":
                i += 1
            if cmd == "UP":
                i -= 1
            if cmd == "LEFT":
                j -= 1
            if cmd == "RIGHT":
                j += 1

        return matrix[i][j]
