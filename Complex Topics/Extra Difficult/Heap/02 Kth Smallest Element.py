import heapq

def kth_smallest(nums, k):
    # Step 1: Create a max heap with first k elements (negate to simulate max-heap)
    max_heap = [-num for num in nums[:k]]
    heapq.heapify(max_heap)

    # Step 2: Process the rest of the elements
    for num in nums[k:]:
        if -num > max_heap[0]:  # If current num is smaller than the largest in heap
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    # Step 3: Return the root of the heap (negate back)
    return -max_heap[0]
