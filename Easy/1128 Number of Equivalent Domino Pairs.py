# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        winner = None
        matrix = [[0 for _ in range(3)] for _ in range(3)]

        # use 1 for the first player move, 5 — the second player
        # winner sum on row/col/diagonal == 3(1+1+1) or 15(5+5+5)
        for i, (x, y) in enumerate(moves):
            matrix[x][y] = 5 if i & 1 else 1

        def checkWin(s):
            nonlocal winner
            if winner: return
            if s == 3: winner = 'A'
            if s == 15: winner = 'B'

        def checkRows():
            for row in matrix: checkWin(sum(row))

        def checkCols():
            for col in zip(*matrix): checkWin(sum(col))

        def checkDiagonal1():
            checkWin(matrix[0][0] + matrix[1][1] + matrix[2][2])

        def checkDiagonal2():
            checkWin(matrix[0][2] + matrix[1][1] + matrix[2][0])

        checkRows()
        checkCols()
        checkDiagonal1()
        checkDiagonal2()

        return winner or ('Draw' if len(moves) == 9 else 'Pending')
        
