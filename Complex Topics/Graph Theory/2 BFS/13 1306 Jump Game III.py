# https://leetcode.com/problems/jump-game-iii/description/

from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)

        q = deque()
        q.append(start)

        visited = set()

        while q:

            curr = q.popleft()

            if curr in visited:
                continue

            if arr[curr] == 0:
                return True

            index = curr + arr[curr]
            if index >= 0 and index < n:
                q.append(index)

            index = curr - arr[curr]
            if index >= 0 and index < n:
                q.append(index)
                
            visited.add(curr)

        return False
        
