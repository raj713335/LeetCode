# https://leetcode.com/problems/ipo/description/

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        ptr = 0

        profits_arr = zip(capital, profits)
        profits_arr = sorted(profits_arr)

        q = []
        heapq.heapify(q)

        for i in range(k):
            while ptr < n and profits_arr[ptr][0] <= w:
                heappush(q, -profits_arr[ptr][1])
                ptr += 1
            if not q:
                break

            w += -heappop(q)

        return w
