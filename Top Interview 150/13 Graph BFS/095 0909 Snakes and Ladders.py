# https://leetcode.com/problems/snakes-and-ladders/description/

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)
        board = board[::-1]

        def intToPos(Square):
            r = (Square - 1) // length
            c = (Square - 1) % length

            if r % 2 == 1:
                c = length - 1 - c

            return r, c

        
        visited = set()
        q = deque()
        q.append([1, 0])

        while q:

            Square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = Square + i

                r, c = intToPos(nextSquare)

                if board[r][c] != -1:
                    nextSquare = board[r][c]
                  
                if nextSquare == (length * length):
                    return moves + 1

                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1            
