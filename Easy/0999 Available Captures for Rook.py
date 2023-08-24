# https://leetcode.com/problems/available-captures-for-rook/description/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        n = 8 

        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == "R":
                    x, y = i, j
                    break

        count = 0
        for i in range(x, -1, -1):
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                count += 1
                break

        for i in range(x, 8, 1):
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                count += 1
                break
        
        for i in range(y, -1, -1):
            if board[x][i] == "B":
                break
            if board[x][i] == "p":
                count += 1
                break

        for i in range(y, 8, 1):
            if board[x][i] == "B":
                break
            if board[x][i] == "p":
                count += 1
                break

        return count
        
