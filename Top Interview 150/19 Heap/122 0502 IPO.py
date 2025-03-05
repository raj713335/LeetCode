# https://leetcode.com/problems/ipo/description/

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)

        projects = zip(capital, profits)
        projects = sorted(projects)

        max_heap = []
        index = 0

        for _ in range(k):

            while index < n and projects[index][0] <= w:
                heapq.heappush(max_heap, - projects[index][1])
                index += 1

            if not max_heap:
                break

            w += - heapq.heappop(max_heap)

        return w
