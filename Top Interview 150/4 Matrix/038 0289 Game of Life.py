# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        h = len(board)
        w = len(board[0])

        dictx = {}

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                neighbours = []

                if i-1 >= 0 and j-1 >= 0:
                    neighbours.append(board[i-1][j-1])

                if i-1 >= 0:
                    neighbours.append(board[i-1][j])

                if i-1 >= 0 and j+1 < w:
                    neighbours.append(board[i-1][j+1])

                if j-1 >= 0:
                    neighbours.append(board[i][j-1])

                if j+1 < w:
                    neighbours.append(board[i][j+1])

                if i+1 < h and j-1 >= 0:
                    neighbours.append(board[i+1][j-1])

                if i+1 < h:
                    neighbours.append(board[i+1][j])

                if i+1 < h and j+1 < w:
                    neighbours.append(board[i+1][j+1])


                live = neighbours.count(1)
                dead = neighbours.count(0)

                dictx[(i, j)] = [live, dead]

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                live, dead = dictx[(i, j)]

                if live < 2:
                    board[i][j] = 0
                if live > 3:
                    board[i][j] = 0
                if live == 3:
                    board[i][j] = 1

