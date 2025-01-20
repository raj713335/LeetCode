# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        min_heap = []
        result = []
        
        # Initialize the heap with pairs from nums1[0] and each element in nums2
        for j in range(min(k, len(nums2))):  # Limit to k elements from nums2
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        # Extract the smallest pairs up to k times
        while k > 0 and min_heap:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If possible, add the next pair involving nums1[i + 1] and nums2[j]
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            k -= 1
        
        return result
        
