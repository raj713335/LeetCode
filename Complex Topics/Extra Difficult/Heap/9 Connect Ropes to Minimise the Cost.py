# Time: O(n log n) — for heap operations
#Space: O(n) — heap space


import heapq

def connectRopes(ropes):
    heapq.heapify(ropes)  # Min-heap of rope lengths
    total_cost = 0

    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)

    return total_cost


ropes = [4, 3, 2, 6]
print(connectRopes(ropes))  # Output: 29

# Step 1: Combine 2 + 3 = 5   → cost = 5
# Step 2: Combine 4 + 5 = 9   → cost = 5 + 9 = 14
# Step 3: Combine 6 + 9 = 15  → cost = 14 + 15 = 29

