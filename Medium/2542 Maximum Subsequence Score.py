# https://leetcode.com/problems/maximum-subsequence-score/description/

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        n = len(nums1)
        pairs = sorted(zip(nums2, nums1), reverse=True)  # Sort by nums2 descending

        min_heap = []
        total = 0
        max_score = 0

        for num2, num1 in pairs:
            heapq.heappush(min_heap, num1)
            total += num1

            if len(min_heap) > k:
                total -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, total * num2)

        return max_score
        
