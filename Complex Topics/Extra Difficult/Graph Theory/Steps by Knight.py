# https://www.geeksforgeeks.org/problems/steps-by-knight5927/


from collections import deque

class Solution:
    def is_valid(self, x, y, n, visited):
        return 1 <= x <= n and 1 <= y <= n and not visited[x][y]
    
    def minStepToReachTarget(self, knightPos, targetPos, n):
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        
        visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        
        q = deque()
        q.append((knightPos[0], knightPos[1], 0))
        visited[knightPos[0]][knightPos[1]] = True
        
        while q:
            x, y, steps = q.popleft()
            if [x, y] == targetPos:
                return steps
            
            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, n, visited):
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, steps + 1))
        
        return -1
