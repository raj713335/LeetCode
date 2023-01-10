# https://leetcode.com/problems/distance-between-bus-stops/description/


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start < destination:

            return min(sum(distance[start:destination]), (sum(distance[0:start])+sum(distance[destination:])))
        else:
            return min(sum(distance[destination:start]), (sum(distance[0:destination])+sum(distance[start:])))
