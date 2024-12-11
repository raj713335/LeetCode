# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            val = list(filter(lambda x: (x != "."), board[i]))
            if len(val) != len(set(val)):
                return False

        for i in range(0, len(board)):
            dixtc = {}
            for j in range(0, len(board[0])):
                if board[j][i] != ".":
                    if board[j][i] in dixtc:
                        return False
                    else:
                        dixtc[board[j][i]] = 1

        for i in range(0, len(board)-2,3):
            for j in range(0, len((board[0]))-2,3):
                temp = [board[i][j], board[i+1][j], board[i+2][j], board[i][j+1], board[i+1][j+1], board[i+2][j+1],
                        board[i][j+2], board[i+1][j+2], board[i+2][j+2]]
                temp = list(filter(lambda x: x != ".", temp))
                if len(temp) != len(set(temp)):
                    return False

        return True