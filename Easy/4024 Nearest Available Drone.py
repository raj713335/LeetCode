# https://leetcode.com/problems/nearest-available-drone/description/


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:

        listx = []

        for i in range(0, len(drones)):

            res = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])

            if drones[i][2] >= res:
                listx.append([i, res])

        x = list(sorted(listx, key=lambda x: x[1]))

        try: 
            return x[0][0]
        except:
            return -1

        
        
