# Time: O(n + k log n) ≈ O(n) for heapify + O(k log n) for popping
# Space: O(n) for heap

import heapq

def sum_between_k1_k2(arr, k1, k2):
    heapq.heapify(arr)
    total = 0

    # pop k1 smallest
    for _ in range(k1):
        heapq.heappop(arr)
    
    # sum next (k2 - k1 - 1) elements
    for _ in range(k2 - k1 - 1):
        total += heapq.heappop(arr)
    
    return total


arr = [1, 3, 12, 5, 15, 11]
print(sum_between_k1_k2(arr, 3, 6))  # Output: 23

