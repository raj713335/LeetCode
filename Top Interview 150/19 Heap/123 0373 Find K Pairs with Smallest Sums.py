# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        res = []

        for j in range(0, len(nums2)):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        while k > 0 and min_heap:
            sumx, i, j = heapq.heappop(min_heap)

            res.append([nums1[i], nums2[j]])

            if (i+1) < len(nums1):
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))
            k -= 1

        return res
