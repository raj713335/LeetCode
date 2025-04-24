import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Count frequencies
    freq_map = Counter(nums)

    # Step 2: Build a min-heap of size k
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements from heap
    return [num for freq, num in heap]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]

# Time: O(n log k) — n for counting, log k for heap operations.
# Space: O(n) — for frequency map and heap.

## Variation: Return in Frequency Descending Order

def topKFrequentSorted(nums, k):
    freq_map = Counter(nums)
    max_heap = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(max_heap)
    return [heapq.heappop(max_heap)[1] for _ in range(k)]


