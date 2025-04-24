# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        left = 0
        right = n - 1

        total = 0
        left_heap = []
        right_heap = []

        for _ in range(k):
            # Fill left heap
            while len(left_heap) < candidates and left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1

            # Fill right heap
            while len(right_heap) < candidates and left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

            # Compare top of both heaps
            if right_heap and (not left_heap or left_heap[0][0] > right_heap[0][0] or 
                            (left_heap[0][0] == right_heap[0][0] and left_heap[0][1] > right_heap[0][1])):
                cost, _ = heapq.heappop(right_heap)
            else:
                cost, _ = heapq.heappop(left_heap)

            total += cost

        return total
