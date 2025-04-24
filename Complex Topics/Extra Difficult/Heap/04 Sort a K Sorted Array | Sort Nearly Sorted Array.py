# Time: O(n log k)
# Space: O(k)



import heapq

def sort_k_sorted_array(arr, k):
    n = len(arr)
    heap = arr[:k+1]
    heapq.heapify(heap)

    target_index = 0
    for i in range(k+1, n):
        arr[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        target_index += 1

    while heap:
        arr[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr


arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(sort_k_sorted_array(arr, k))
# Output: [2, 3, 5, 6, 8, 9, 10]

