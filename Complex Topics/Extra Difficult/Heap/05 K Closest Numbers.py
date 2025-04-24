# For Unsorted Array — Use a Max-Heap

import heapq

def kClosestNumbers(arr, k, x):
    max_heap = []

    for num in arr:
        dist = abs(num - x)
        heapq.heappush(max_heap, (-dist, -num))  # Max-heap trick

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    result = [-num for _, num in max_heap]
    return sorted(result)

arr = [4, 1, 3, 7, 10, 5]
k = 3
x = 6
print(kClosestNumbers(arr, k, x))  # Output: [4, 5, 7]




# Efficient Approach for Sorted Array (Two Pointers + Binary Search):

# Time: O(log(n - k) + k)
# Space: O(1) extra

def findClosestElements(arr, k, x):
    # Binary search for the closest left index
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # Compare distances from x
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]
