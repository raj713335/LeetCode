# Frequency Sort for a List of Integers using heapq

import heapq
from collections import Counter

def frequencySortArray(nums):
    freq = Counter(nums)
    
    # max-heap: use negative frequency
    max_heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        count, num = heapq.heappop(max_heap)
        result.extend([num] * -count)  # multiply the number by its frequency

    return result

print(frequencySortArray([1,1,2,2,2,3]))
# Output: [2,2,2,1,1,3]

# Frequency Sort for a String using heapq

import heapq
from collections import Counter

def frequencySortString(s):
    freq = Counter(s)

    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char * -count)

    return ''.join(result)

print(frequencySortString("tree"))
# Output: "eetr" or "eert"

