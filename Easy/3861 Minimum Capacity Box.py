# https://leetcode.com/problems/minimum-capacity-box/description/


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        

        minimum_capacity = math.inf
        minimum_capacity_index = -1

        for i in range(0, len(capacity)):

            if capacity[i] >= itemSize and minimum_capacity > capacity[i]:
                minimum_capacity = capacity[i]
                minimum_capacity_index = i

        return minimum_capacity_index
