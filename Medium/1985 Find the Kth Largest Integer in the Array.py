# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        min_heap = []

        count = 0

        for num in nums:
            heapq.heappush(min_heap, int(num))
            count += 1
            if count > k:
                heapq.heappop(min_heap)

        return str(min_heap[0])
        
